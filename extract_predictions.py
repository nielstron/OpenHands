import json

import sys
import os
from unidiff import PatchSet
import logging

_LOGGER = logging.getLogger(__name__)

prediction_dir = sys.argv[1]
# prediction_dir = "evaluation/evaluation_outputs/outputs/princeton-nlp__SWE-bench_Lite-test/CodeActAgent/claude-3-5-sonnet-20241022_maxiter_30_N_v0.23.0-no-hint-testrun1/output.jsonl"
predictions = []

# extract everything under "2025-02-12 17:11:03,241 - INFO - Got git diff for instance astropy__astropy-6938:"

with open(prediction_dir) as f:
    for line in f:
        pred = json.loads(line)
        git_diff = pred["test_result"]["git_patch"]
        try:
            patchset = PatchSet(git_diff)
        except:
            _LOGGER.warning("No git diff found for instance %s", pred["instance_id"])
            continue
        try:
            print(json.dumps({
                "instance_id": pred["instance_id"],
                "model_name_or_path": "OpenHands-Claude-Sonnet-3.5",
                "model_patch": git_diff,
                "full_output": json.dumps(pred),
            }))
        except KeyError:
            _LOGGER.warning("No git diff found for instance %s", pred["instance_id"])

