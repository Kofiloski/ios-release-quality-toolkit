---
summary: Maintain native Simulator checks, scoped runtime diagnostics, and current Apple review-policy sources without changing the reusable CI contract.
read_when:
  - Updating Simulator verification modes or Xcode tool guidance
  - Updating log, persisted-state, or runtime diagnostic guidance
  - Updating the App Store review skill or its policy references
---

# Simulator and policy maintenance

The toolkit remains a skills-only plugin. Local Simulator exploration belongs in `ios-ai-ui-check`; app-side accessibility repairs belong in `ios-ui-testability-contract`. Both use capabilities exposed by the connected Xcode instead of hard-coding a tool catalog or requiring another MCP server. The CI action and app-owned scenario runner retain their existing execution and artifact contracts.

Each canonical project now owns an installable bundle under `skills/<name>/`: [App Store Review Risk](https://github.com/Kofiloski/app-store-review-risk), [UI Testability Contract](https://github.com/Kofiloski/ios-ui-testability-contract-skill), and [iOS AI UI Check](https://github.com/Kofiloski/ios-ai-ui-check). This toolkit embeds separate copies. When changing a bundled skill, port the applicable guidance upstream, check both repositories, align executable pins with their releases, and compare bundle contents before publishing. A toolkit release alone does not update upstream repositories, PyPI packages, or already installed local skills.

The App Review and UI Check Actions also have GitHub Marketplace listings linked from the README. Verify those public listings after upstream Action releases; GitHub release creation and PyPI publication do not establish that Marketplace shows the intended version. Follow each upstream release guide if the listing needs publication. Marketplace link and documentation updates alone do not require a new toolkit version or moving existing tags.

Xcode 27 introduced native agent tools for Simulator boot, app installation/launch, touch input, and screenshots ([release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), issue 175179787). External agents connect using Apple's [MCP bridge setup](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode). Discover tool schemas at runtime: an installed Xcode version alone does not establish session capabilities. Local screenshots and touch actions cannot establish XCTest identifier/type correctness; an accessibility-contract repair still requires inspection and replay through the failing automation tool.

`ios-ai-ui-check/references/simulator-diagnostics.md` owns the optional local diagnostic procedure: correlate one reproduction with app-filtered logs, relevant persisted state, and focused runtime inspection. The testability skill applies the same evidence boundary in `references/verification-loop.md`; the review skill uses `references/runtime-evidence.md` for reviewer-facing flows. Prefer installed Xcode, `simctl`, and app-owned helpers. No Simulator jailbreak, injection tool, new CLI, or CI artifact requirement is introduced. Keep raw data outside shared/planner artifacts and instrumented results separate from normal replay. See [simulator-test-app.md](simulator-test-app.md) for the pinned evaluation app and distinguish source inspection from live execution.

Do not assume AXe, XcodeBuildMCP, another MCP server, or a companion CLI is available. Xcode/XCTest and Apple's command-line tools provide the supported local path; discover optional capabilities rather than requiring them. Read any workflow guidance returned by the connected Xcode tools, including a relevant Xcode-bundled skill. If a native interaction workflow requires delegation that the host cannot provide, use the available XCTest route or report the gap. The toolkit does not bundle those external tools or configure their permissions.

`app-store-review-risk` retrieves the live guidelines and latest official update notice for every review. Its `references/current-policy.md` owns this procedure. The pinned scanner and bundled risk maps help find evidence but cannot establish the current policy baseline. Reports distinguish the retrieval date from Apple's displayed revision date and disclose unavailable sources. Keep storefront exceptions, submission deadlines, and entitlement terms tied to live Apple sources rather than turning them into permanent scanner assumptions.

On October 28, 2026, the [live guidelines](https://developer.apple.com/app-store/review/guidelines/) displayed an October 16, 2026 revision. Apple's [announcement](https://developer.apple.com/news/?id=92th7e5i) identified changes to UGC scope/safeguards, creative assets (2.3.14), hidden features (2.5.19), and external purchase links (3.1.1(a)), among others. This dated maintenance evidence explains the update; it is not the baseline for future reviews. Future invocations fetch the sources again.

Validate changes with the repository checker and unit tests from the README, the skill-creator validator for changed skills, and `docs-list . --strict`. For behavior review, check that local requests avoid unsolicited CI scaffolding, native touch success cannot substitute for an XCUITest replay, new policy changes can be reviewed without scanner support, and unavailable live guidance is disclosed rather than presented as current compliance.

## Planner configuration guidance

Toolkit `v0.2.3` bundles UI Check `v0.6.0` guidance for explicit provider, model, and effort choices, including native Anthropic planning. Keep the skill copy byte-identical to its canonical source. Consumers must deliberately refresh app-managed scripts and adopt the `v0.6.0` action before using the new selection flags. Skill installation does not change the coding-agent session's own provider/model/effort or upgrade app scripts. Fixture tests do not establish live Claude access; hosted workflow checks and credentialed planner calls are separate evidence. See the action's [pinned planner configuration](https://github.com/Kofiloski/ios-ai-ui-check/blob/v0.6.0/docs/planner-configuration.md).
