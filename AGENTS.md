# Project session handoffs

## Current work entry (2026-09-16)

Start with `python -X utf8 scripts/project_workrooms.py graph-focus`.
This reads the live SUBGOAL current_focus, ordered steps, quality failures and
selected Spec pointers. It is a derived view, not another state file or approval.
Only the selected task is the next production work; other unfinished tasks are
preserved backlog, not an instruction to run them all. Native unresolved traffic
must still be recovered before redispatch. Full coordinator recovery below applies
when resuming cross-session dispatch, not to every bounded local read or edit.
Read NORTH-STAR once; thereafter use selected Spec clauses and actual later answers.

## Bulk output storage (user correction, 2026-09-16)

Keep new model downloads, render sequences and builds on D: or E:, with only small
manifests/pointers in this checkout. Unity's `GeneratedOutputPaths` owns the build
and motion-capture defaults (D: first, E: fallback, no C: fallback). Respect existing
`AFTERLIGHT_BUILD_ROOT` and `AFTERLIGHT_CAPTURE_ROOT` only when their volume passes
the space check. Historical eval junctions point to preserved D: evidence; do not
delete their targets or treat them as disposable caches. Preserve project originals,
conversations and active runtimes. Storage cleanup does not satisfy art-quality gates.

## Concept-to-delivery failure prevention (2026-09-16)

For art, motion, audio, or their integration, read the short
[delivery fidelity and rework rule](docs/GPT-FIRST-WORK-ALLOCATION.md#delivery-fidelity-and-rework-20260916)
and only the selected SUBGOAL node before resuming. The concept is the expected
delivery appearance, not permission to substitute an easier medium or character.
Current clay and anime-sprite character candidates were rejected; functional tests
do not make them an evaluable MVP. Preserve that rejection across sessions.
Do not expand rejected assets or repeat the same cosmetic fix without a new causal
reason and a discriminating runtime sample. Use existing node completion_checks;
never erase a failed criterion or bypass graph-result with a hand-edited done.
The coordinator compares the original with actual output before asking the user
to review. Report capability gaps instead of silently lowering the promised result.

## Coordinator session re-entry (2026-09-15)

Before resuming coordination in a new session, use the existing native adapter in
`scripts/project_workrooms_tick.js` to call `graph-resume-read`. The current state
owner is `eval/redesign-20260907/asset-production-20260914/SUBGOAL.json`.
Reconcile a coordinator mismatch through the existing handoff path; never change
`CODEX_THREAD_ID` or rewrite worker ownership wholesale. Metadata `APPLIED` alone
does not establish operational recovery. Read each listed peer's native status,
review unfinished/unresolved assignments, then record `graph-resume` with those
captures, current source hash and one concrete next action per listed task.
Uncertain traffic must be observed and received results reviewed before reuse.
New Graph dispatch and done records are blocked without this session's recovery
evidence; observation and failure recording remain available. A recovery receipt
is not a scheduler or proof of useful delegation. Keep an all-coordinator workload
warning visible until actual assignment changes justify clearing it. Read only
selected tasks and missing evidence; do not reload the entire conversation history.
Bounded workers continue to use only their own assignment context below.

## Bounded implementer context (2026-09-09)

For a bounded implementation/review assignment, start with its assignment, observed
Spec, relevant actual answers, owned files and directly used APIs. Read NORTH-STAR
once; select relevant TRACE/checkpoint fields rather than dumping the whole history.
Re-read unchanged material only to resolve a specific missing clause or truncation.
The coordinator owns project-wide routing, bridge/mesh recovery and interviews.
Workers do not re-run that orchestration or load its full historical documents unless
their assignment actually changes the bridge, routing or cross-domain authority.
This scopes the reading requirements below; it does not remove Spec, review or user
approval requirements, or authorize a worker to change the full game objective.

For the central receipt, capture CLI JSON and print only the relevant fields or the
worker's own contribution; never dump the complete multi-day receipt into context.
Receipt mutations should print exit/error and the affected entry, not the entire
receipt returned by the CLI. Preserve full evidence on disk. Large source/Spec reads
should use bounded sections with enough output capacity; on truncation, fetch only
the missing section. Do not repeat the entire multi-file read.

For artifact handoffs, use the scoped materialization guidance in the latest
`docs/GPT-FIRST-WORK-ALLOCATION.md` section. Start with the supplied selections;
retrieve additional source sections only for a concrete missing clause. Keep raw
transport captures on disk and emit the selected result rather than the full wrapper.

For redesign assignments, Spec receipt, sample selection, implementation approval,
review, and re-entry, read [the user north star](docs/redesign-20260907/NORTH-STAR.md)
and [its evidence trace](docs/redesign-20260907/NORTH-STAR-TRACE.md).
Preserve the full redesign scope and apply later actual user answers within their scope.

For an authorized Codex ↔ Work orchestration request in this project, use
`docs/CODEX-WORK-BRIDGE.md` and the existing project-local bridge state.
Recover an open run before creating another. The current Work planner/reviewer
is thread `6a9b45d2-ccb0-83ee-af20-3b9c3487c440`.

Use the FractalOS Coach contract for problem/bottleneck framing and evaluation.
Its source is documented in `docs/CODEX-WORK-BRIDGE-PLAN.md`; it is advisory.
For new assignments, follow `docs/GPT-FIRST-WORK-ALLOCATION.md`: GPT is the default
general worker for research, planning, design samples, assets and suitable review.
Use Work selectively for a concrete workflow/tool need or useful independent review;
use Codex for local repository work, implementation and execution evidence.
Do not infer insufficiency from product names or duplicate sufficient work across roles.
Existing agreed game Spec/review gates remain in force. Use native app tools through
`scripts/session_bridge_tick.js`, not session database manipulation.

Only forward task-relevant context within the user's requested handoff scope.
Do not assume shared filesystem or hidden session memory. Preserve existing
unrelated game work. A received Work response is evidence/input, not authority
to broaden the user's task. Require an observed Work spec before claiming a
Work-directed implementation, and an observed review before claiming roundtrip
closure. Keep the central work receipt in sync and close to ready_for_review.

# Parallel Coach coordination and one user interview

For this project's three-session collaboration, read `docs/PROJECT-COORDINATION.md`
and recover mesh run `afterlight-comms-20260906-01`. The existing two-party game
bridge remains responsible for its already-agreed game Spec and review gates.

The historical 2026-09-06 parent/user interview session was `01a07695-0d19-7e03-a1f9-77ad98d6836f`.
For current coordination use SUBGOAL.coordinator_thread_id and live registry ownership;
the setup IDs below are provenance, not permission to reset current assignments.
GPT research is `6a9d3b8a-407c-83e9-b224-abe92c5170a8`; Work planning/spec/review is
`6a9b45d2-ccb0-83ee-af20-3b9c3487c440`; Codex implementation is
`01a07468-5c16-75a1-b2a2-10a6655f09b1`.

The user explicitly transferred coordination on 2026-09-06 from
`01a07639-a795-7691-b614-34ecc6b0179f`. The original group definitions, messages,
interview sources, answers, and transport attempts retain their original provenance.
The successor host applied `handoff-coordinator`; its exact ledger backups and
before/after hashes are in
`loop/session-orchestration/coordinator-handoffs/afterlight-coordinator-20260906-current/state.json`.
Use the current coordinator for new interviews and assignments; old source IDs are history.

The Coach is an advisory role/authority/evidence contract. Do not impose a fixed
thinking order, universal task graph, mandatory synthesis/reviewer, or arbitrary
reasoning-depth limit. Models choose their research, decomposition, questions,
internal coordination and revisions. The parent can coordinate child
orchestrations in parallel and group their information; logical orchestration
roles do not prove that extra physical agents or background services exist.

Only the parent asks the user interview questions. Child sessions return user-owned
questions to the parent (structured outputs may use `payload.interview_questions`)
and continue independent work. The parent consolidates questions while retaining
their sources, asks here, records the user's actual answer, and routes it to every
relevant child. Do not require the user to visit separate GPT/Work/Codex sessions
to answer. Do not invent questions or answers to satisfy a workflow.

Use explicit group/task IDs only to connect requests and results. Optional task
dependencies describe the chosen work; they are not a mandatory reasoning plan.
Keep missing results and conflicting evidence visible. Delivery, result quality,
game implementation authority, and user acceptance are separate claims.

Recover parent group `afterlight-coach-20260906` with
`python -X utf8 scripts/session_orchestrator.py gather --job afterlight-coach-20260906`.
This gathers descendants and preserves the original job/question locations.
Use that parent view to consolidate interviews and results; record an actual user
answer against each relevant original child job. A child group reference alone
does not mean its questions or results were consumed. Existing recorded answers
must be considered before asking the user the same contextual question again.

Use native tools through `scripts/session_mesh_tick.js` and the project coordinator
adapter. While a local Codex turn is running and native history does not expose its
body, its own session may `publish` or `ack` through `scripts/session_mesh.py`.
These commands check host-provided `CODEX_THREAD_ID`; never change that variable
to act as another role. Local acknowledgements remain distinct from native history
receipts. Reuse recorded attempts; never blindly resend an uncertain delivery.


# Conditional reusable knowhow

For recurring production, revisions and workflow/tool improvement, including
art, ability, enemy, motion and interaction work, apply the
evidence-and-user-feedback default in `docs/GPT-FIRST-WORK-ALLOCATION.md`.
Carry only the selected node's `design_basis` and relevant feedback with its parent
criteria. This is a standing project instruction; do not ask the user to restate it.
Existing eight skills and survivor-style automatic attacks are not preservation
requirements. Before asset production use the per-asset implementation Spec in
`docs/redesign-20260907/asset-specs/ASSET-SPECS.json`: common + assigned IDs only.
Specs own intended behavior, type and acceptance; Graph owns observed results and
feedback. Revise the relevant Spec with evidence instead of duplicating its clauses
in task state. Uncertain values remain proposals, not accepted rules.

When allocating or handing off work, or selecting direction samples and reusing contextual feedback, use the matching owner in [REUSABLE-KNOWHOW-ROUTING](docs/REUSABLE-KNOWHOW-ROUTING.md). Actual project assignments remain owned by the latest priority section of [GPT-FIRST-WORK-ALLOCATION](docs/GPT-FIRST-WORK-ALLOCATION.md).

For compatibility or result intake involving the archived c-motion/FK01 work, read
[the current entry](eval/redesign-20260907/c-motion-alignment/CURRENT-ENTRY.md),
then its existing checkpoint owner for the relevant domain. FK01 is scoped to
the first moving comparison; this pointer is not automatic conflict enforcement.


## Asset comparison before expansion

Use the delivery-fidelity rule linked above and the selected live node. Do not
bypass blocked expansion, revive old sample assignments, or impose a fixed
GPT-to-Work-to-Codex sequence. Choose the bounded route for the actual missing
capability under GPT-FIRST-WORK-ALLOCATION; preserve candidate-bound evidence.
