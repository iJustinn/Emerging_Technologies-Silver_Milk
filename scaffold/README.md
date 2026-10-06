# ET Scaffold Working Copy (not committed)

**Decided D-12 (Lab 3):** the repo stays public, so the scaffold is never committed here. The full package, scaffold included, is the Brightspace ZIP for each lab. The steps below apply only if D-12 is reopened.

**Status: BLOCKER / pending input.** `MASY1800_ET_Agent_Scaffold_v1_0.zip` is not yet in the team workspace.

When it is available:

0. **Gate:** do not commit the scaffold while this repo is public. First make the repo private, or get instructor approval (issue I-04).
1. Keep the Brightspace ZIP unchanged. Unzip a working copy into this folder.
2. Before committing, confirm that nothing under `course_materials/` or any other instructor file is caught by `.gitignore`. Do **not** force-add ignored files, because this repo is public.
3. Run `python tools/check_frozen_core.py` and paste the output into `records/test_failure_log.md`.
4. Commit it unchanged as `Add unchanged ET scaffold v1.0 working copy`.
5. Re-confirm the FROZEN CORE file list in `docs/team_agent_standard.md` Section 1 against this scaffold's `FROZEN_CORE_SHA256.txt`.

Team Lab 2 exercised the workflow on the Chart Improvement Practice Scaffold v1.0 instead (see `records/test_failure_log.md`).
