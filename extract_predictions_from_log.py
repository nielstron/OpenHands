import json

import sys
import os
from unidiff import PatchSet
import logging

_LOGGER = logging.getLogger(__name__)

prediction_dir = sys.argv[1]
# prediction_dir = "evaluation/evaluation_outputs/outputs/princeton-nlp__SWE-bench_Lite-test/CodeActAgent/claude-3-5-sonnet-20241022_maxiter_30_N_v0.23.0-no-hint-testrun1/infer_logs"
predictions = []

# extract everything under "2025-02-12 17:11:03,241 - INFO - Got git diff for instance astropy__astropy-6938:"

for instance in os.listdir(prediction_dir):
    with open(os.path.join(prediction_dir, instance)) as f:
        instance_name = "_".join(instance.split(".")[0].split("_")[1:])
        log = f.readlines()
    try:
        git_diff_start_line = next(i for i, l in enumerate(log) if "INFO - Got git diff for instance" in l)
    except StopIteration:
        _LOGGER.warning("No git diff found for instance %s", instance)
        continue
    try:
        git_end_line = next(i for i, l in enumerate(log[git_diff_start_line+3:]) if "--------" == l.strip())
    except StopIteration:
        git_end_line = -1
    git_diff = "".join(log[git_diff_start_line+2:git_end_line]).strip()
    # check if diff is valid
    try:
        patchset = PatchSet(git_diff)
    except:
        _LOGGER.warning("No git diff found for instance %s", instance)
        continue
    print(json.dumps({
        "instance_id": instance_name,
        "model_name_or_path": "OpenHands-Claude-Sonnet-3.5",
        "model_patch": git_diff,
        "full_output": "\n".join(log),
    }))

