---
summary: Maintain native Xcode Simulator routing and current Apple review-policy sources without changing the reusable CI contract.
read_when:
  - Updating Simulator verification modes or Xcode tool guidance
  - Updating the App Store review skill or its policy references
---

# Simulator and policy maintenance

The toolkit remains a skills-only plugin. Local Simulator exploration belongs in `ios-ai-ui-check`; app-side accessibility repairs belong in `ios-ui-testability-contract`. Both use capabilities exposed by the connected Xcode instead of hard-coding a tool catalog or requiring another MCP server. The CI action and app-owned scenario runner retain their existing execution and artifact contracts.

Xcode 27 introduced native agent tools for Simulator boot, app installation/launch, touch input, and screenshots ([release notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes), issue 175179787). External agents connect using Apple's [MCP bridge setup](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode). Discover tool schemas at runtime: an installed Xcode version alone does not establish session capabilities. Local screenshots and touch actions cannot establish XCTest identifier/type correctness; an accessibility-contract repair still requires inspection and replay through the failing automation tool.

`app-store-review-risk` retrieves the live guidelines and latest official update notice for every review. Its `references/current-policy.md` owns this procedure. The pinned scanner and bundled risk maps help find evidence but cannot establish the current policy baseline. Reports distinguish the retrieval date from Apple's displayed revision date and disclose unavailable sources. Keep storefront exceptions, submission deadlines, and entitlement terms tied to live Apple sources rather than turning them into permanent scanner assumptions.

On October 28, 2026, the [live guidelines](https://developer.apple.com/app-store/review/guidelines/) displayed an October 16, 2026 revision. Apple's [announcement](https://developer.apple.com/news/?id=92th7e5i) identified changes to UGC scope/safeguards, creative assets (2.3.14), hidden features (2.5.19), and external purchase links (3.1.1(a)), among others. This dated maintenance evidence explains the update; it is not the baseline for future reviews. Future invocations fetch the sources again.

Validate changes with the repository checker and unit tests from the README, the skill-creator validator for changed skills, and `docs-list . --strict`. For behavior review, check that local requests avoid unsolicited CI scaffolding, native touch success cannot substitute for an XCUITest replay, new policy changes can be reviewed without scanner support, and unavailable live guidance is disclosed rather than presented as current compliance.
