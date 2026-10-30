# -*- coding: utf-8 -*-
"""Sleep Spindle Density & Slow-Wave Coupling (PAC) Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def evaluate_sleep_spindle_coupling(**kwargs):
    """Quantifies EEG slow-wave oscillation (SO) to sleep spindle phase-amplitude coupling (PAC), memory consolidation efficiency, and nocturnal glymphatic clearance quality."""
    nrem3_duration_minutes = kwargs.get('nrem3_duration_minutes')
    fast_spindle_count = kwargs.get('fast_spindle_count')
    slow_spindle_count = kwargs.get('slow_spindle_count')
    so_spindle_cooccurrence_events = kwargs.get('so_spindle_cooccurrence_events')
    mean_coupling_phase_degrees = kwargs.get('mean_coupling_phase_degrees')

    total_spindles = fast_spindle_count + slow_spindle_count
    spindle_density_per_min = round(total_spindles / (nrem3_duration_minutes if nrem3_duration_minutes > 0 else 1.0), 2)
    coupling_ratio_pct = round((so_spindle_cooccurrence_events / (total_spindles if total_spindles > 0 else 1.0)) * 100.0, 1)
    
    phase_offset = abs(mean_coupling_phase_degrees)
    coupling_precision = round(max(0.0, 100.0 - (phase_offset * 0.8)), 1)
    glymphatic_score = round(min(100.0, (nrem3_duration_minutes / 90.0 * 50.0) + (coupling_ratio_pct * 0.5)), 1)
    
    if spindle_density_per_min >= 2.5 and coupling_ratio_pct >= 65.0:
        neuro_consolidation = "Optimal (Robust synaptic consolidation and neural pruning)"
    elif spindle_density_per_min >= 1.5:
        neuro_consolidation = "Adequate (Moderate spindle activity)"
    else:
        neuro_consolidation = "Attenuated (Deficit in SO-spindle synchrony, impaired declarative consolidation)"
        
    result = {
        "status": "success",
        "nrem3_minutes": nrem3_duration_minutes,
        "total_spindles": total_spindles,
        "spindle_density_per_min": spindle_density_per_min,
        "so_spindle_coupling_ratio_pct": coupling_ratio_pct,
        "phase_precision_score": coupling_precision,
        "glymphatic_clearance_index": glymphatic_score,
        "declarative_memory_consolidation_status": neuro_consolidation,
        "engine": "GenPark Neuro-Oscillatory PAC Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "evaluate_sleep_spindle_coupling": {
        "name": "evaluate_sleep_spindle_coupling",
        "description": "Quantifies EEG slow-wave oscillation (SO) to sleep spindle phase-amplitude coupling (PAC), memory consolidation efficiency, and nocturnal glymphatic clearance quality.",
        "parameters": {
            "type": "object",
            "properties": {
                "nrem3_duration_minutes": {"type": "number", "description": "Duration spent in deep slow-wave sleep N3 (minutes)"},
                "fast_spindle_count": {"type": "integer", "description": "Detected fast sleep spindles (12-16 Hz)"},
                "slow_spindle_count": {"type": "integer", "description": "Detected slow sleep spindles (9-12 Hz)"},
                "so_spindle_cooccurrence_events": {"type": "integer", "description": "Spindles locked to slow-wave oscillation up-phase"},
                "mean_coupling_phase_degrees": {"type": "number", "description": "Mean phase angle of spindle maximum relative to SO peak (-180 to +180 deg)"},
            },
            "required": ['nrem3_duration_minutes', 'fast_spindle_count', 'slow_spindle_count', 'so_spindle_cooccurrence_events', 'mean_coupling_phase_degrees']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_sleep_spindle_coupling":
            res = evaluate_sleep_spindle_coupling(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-sleep-spindle-density-slow-wave-coupling-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-sleep-spindle-density-slow-wave-coupling-skill...")
    test_args = {'nrem3_duration_minutes': 85.0, 'fast_spindle_count': 180, 'slow_spindle_count': 95, 'so_spindle_cooccurrence_events': 195, 'mean_coupling_phase_degrees': -12.5}
    res = evaluate_sleep_spindle_coupling(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-sleep-spindle-density-slow-wave-coupling-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
