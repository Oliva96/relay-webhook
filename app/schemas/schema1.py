schema1 = {
    "type": "object",
    "properties": {
        "event_id": {"type": "string"},
        "event_ts": {"type": "string"},
        "payload": {"type": "object"},
        "event_name": {"type": "string"}
    },
    "required": ["event_id", "event_ts", "payload", "event_name"]
}