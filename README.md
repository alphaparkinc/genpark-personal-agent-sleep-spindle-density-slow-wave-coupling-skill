# Sleep Spindle Density & Slow-Wave Coupling (PAC) Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `evaluate_sleep_spindle_coupling`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Quantifies EEG slow-wave oscillation (SO) to sleep spindle phase-amplitude coupling (PAC), memory consolidation efficiency, and nocturnal glymphatic clearance quality.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Neuro-Sleep Architecture)`

## MCP Tool Specification
### `evaluate_sleep_spindle_coupling`
Parameters:
- `nrem3_duration_minutes` (float): Duration spent in deep slow-wave sleep N3 (minutes)
- `fast_spindle_count` (int): Detected fast sleep spindles (12-16 Hz)
- `slow_spindle_count` (int): Detected slow sleep spindles (9-12 Hz)
- `so_spindle_cooccurrence_events` (int): Spindles locked to slow-wave oscillation up-phase
- `mean_coupling_phase_degrees` (float): Mean phase angle of spindle maximum relative to SO peak (-180 to +180 deg)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-sleep-spindle-density-slow-wave-coupling-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-sleep-spindle-density-slow-wave-coupling-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
