# overlay
Overlay Failure Mind Map 🌿

A thinking aid for calm, systematic overlay troubleshooting

Why this repository exists

In many incident bridges, the first sentence we hear is:

“The overlay is down.”

It sounds like a diagnosis.
Most of the time, it’s panic.

An overlay is not a single thing.
It is a coordination of independent systems that must agree before a packet ever moves.

This repository exists to help engineers debug their thinking first, before debugging packets.

What this is (and what it is not)
✅ This is

A mental model for overlay failure isolation

A way to map symptoms → responsibility

A reminder that decisions fail before packets do

A calm starting point for EVPN / VXLAN / MPLS style overlays

❌ This is not

A troubleshooting automation tool

A replacement for vendor documentation

A packet analysis or monitoring system

A “run this and fix your network” script

Think of this as a map for your mind, not a tool for your device.

Core idea

Most overlay outages fall into one of these responsibility domains:

Control Plane – Was the intent shared?

Data Plane Programming – Was the state programmed into hardware?

Underlay Transport – Could the path actually carry the traffic?

Cross-Layer Dependencies – Are timers, dependencies, or assumptions fighting?

The packet is only the messenger.
The decision to fail usually happened earlier.

overlay/
├── overlay_failure_map.yaml   # Human-readable failure mind map
├── overlay_map.py             # Simple CLI to explore the map
└── README.md                  # You are here


