#!/usr/bin/env python3
"""Format Google Calendar API output into a day-grouped schedule.

Accepts JSON via stdin (the format returned by the Google Workspace MCP tool).
Parses event timestamps, converts to the configured timezone, groups by date,
and outputs a clean day-by-day schedule with verified day names.

Usage:
    echo '<calendar JSON>' | python3 scripts/format-calendar.py
    python3 scripts/format-calendar.py < calendar-data.json
"""

import json
import sys
from datetime import datetime, date
from zoneinfo import ZoneInfo
from collections import defaultdict

# Change this to your timezone
TZ = ZoneInfo("Europe/Paris")

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def parse_event_time(time_obj):
    """Parse a Google Calendar start/end object. Returns (datetime_or_date, is_all_day)."""
    if isinstance(time_obj, str):
        # Plain string - try dateTime then date
        try:
            dt = datetime.fromisoformat(time_obj)
            return dt.astimezone(TZ), False
        except ValueError:
            return date.fromisoformat(time_obj), True

    if isinstance(time_obj, dict):
        if "dateTime" in time_obj:
            dt = datetime.fromisoformat(time_obj["dateTime"])
            return dt.astimezone(TZ), False
        elif "date" in time_obj:
            return date.fromisoformat(time_obj["date"]), True

    raise ValueError(f"Cannot parse time object: {time_obj}")


def get_date_key(parsed_time, is_all_day):
    """Extract a date object for grouping."""
    if is_all_day:
        return parsed_time
    return parsed_time.date()


def format_time(dt):
    """Format a datetime as HH:MM."""
    return dt.strftime("%H:%M")


def format_event(event, start_parsed, end_parsed, is_all_day):
    """Format a single event as a string."""
    summary = event.get("summary", "(No title)")
    location = event.get("location", "")

    if is_all_day:
        line = f"  * [All day] {summary}"
    else:
        line = f"  * {format_time(start_parsed)}\u2013{format_time(end_parsed)} {summary}"

    if location:
        line += f" ({location})"

    return line


def main():
    raw = sys.stdin.read().strip()
    if not raw:
        print("No input provided.", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        print("Invalid JSON input.", file=sys.stderr)
        sys.exit(1)

    # Handle various shapes: list of events, or dict with "items" key
    if isinstance(data, list):
        events = data
    elif isinstance(data, dict):
        events = data.get("items") or data.get("events") or []
        if not events and len(data) == 1:
            # Single key wrapping a list
            events = next(iter(data.values())) if isinstance(next(iter(data.values())), list) else []
    else:
        events = []

    if not events:
        print("No events found in input.")
        sys.exit(0)

    # Parse and group by date
    grouped = defaultdict(list)
    for event in events:
        start = event.get("start")
        end = event.get("end")
        if not start:
            continue

        try:
            start_parsed, is_all_day = parse_event_time(start)
            if end:
                end_parsed, _ = parse_event_time(end)
            else:
                end_parsed = start_parsed
        except ValueError as e:
            print(f"Skipping event: {e}", file=sys.stderr)
            continue

        day = get_date_key(start_parsed, is_all_day)
        grouped[day].append((event, start_parsed, end_parsed, is_all_day))

    # Sort days and events within days
    for day in grouped:
        grouped[day].sort(key=lambda x: (not x[3], x[1] if not x[3] else ""))

    # Output
    for day in sorted(grouped.keys()):
        day_name = DAY_NAMES[day.weekday()]
        print(f"\n### {day_name} {day.strftime('%d %B %Y')}")
        for event, start_parsed, end_parsed, is_all_day in grouped[day]:
            print(format_event(event, start_parsed, end_parsed, is_all_day))


if __name__ == "__main__":
    main()
