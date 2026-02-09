mac_ip_unreachable:
  symptom: "MAC/IP unreachable"
  likely_layer: "Control Plane"
  realization: "The map is wrong"
  checks:
    - "Is EVPN route present?"
    - "Is BGP EVPN session up?"
    - "Is route-type advertised?"
    - "Is RT import/export correct?"

arp_nd_stuck:
  symptom: "ARP / ND unresolved"
  likely_layer: "Data Plane Programming"
  realization: "Hardware ignored the map"
  checks:
    - "Is MAC programmed in ASIC?"
    - "Is NVE interface up?"
    - "Any TCAM exhaustion?"
    - "Is control-plane sync delayed?"

random_drops:
  symptom: "Random packet drops"
  likely_layer: "Underlay Transport"
  realization: "The road is broken"
  checks:
    - "MTU mismatch?"
    - "ECMP hash imbalance?"
    - "Microbursts / buffer drops?"
    - "Link errors?"

slow_recovery:
  symptom: "Slow convergence"
  likely_layer: "Cross-layer dependency"
  realization: "Timers are fighting"
  checks:
    - "IGP timers vs BGP timers?"
    - "EVPN hold timers?"
    - "Graceful restart enabled?"

