# CF-GH-FOLLOW longitudinal update — 2026-09-05

**Status:** follow-on observation record  
**Relationship to the original study:** separate extension; the six-account study in `REPORT.md` remains closed and unchanged.  
**Attribution:** not established.  
**Published narrative:** https://dev.to/gnomeman4201/kept-getting-strange-github-followers-so-i-measured-them-3fac

## Scope boundary

This record documents public observations collected after the original six-account study was closed. It does not retroactively modify that study's frozen protocols, thresholds, exclusions, or final assessment.

The follow-on question is narrower:

> Do later GitHub follower waves reproduce the same higher-order technical artifacts and show a repeatable account-development lifecycle across separate generations?

This is a longitudinal extension, not a claim that every account in every wave has one operator.

## Evidence-strength legend

| Grade | Meaning |
|---|---|
| A | Publicly reproducible immutable Git object or equivalently durable public artifact |
| B | Complete public enumeration or bounded measurement whose arithmetic can be independently checked from the released values |
| C | Longitudinal observation derived from frozen public-state collections; raw collection may remain private/sanitized |
| H | Hypothesis or workflow inference; useful only to the extent that independent observations continue to support it |

No single grade should be read as an attribution score.

## Observed generations

### 1. August 26 five-account wave

Accounts:

- `alberto4442`
- `lxl0825`
- `fuad403273`
- `hassenbrahim`
- `Belucking`

At collection time the accounts exposed roughly 59–60 public repositories each. Across the five owners there were 299 public repositories. Their outbound-following counts were already approximately 7,380–7,695.

Measured characteristics included:

- median repository-creation intervals of roughly 340–346 seconds;
- identical programming-language sequences across all 59 comparable repository positions for three accounts;
- identical first-100 followed-account sets across all five accounts;
- pairwise Jaccard similarity of `1.000` for those first-100 sets;
- the same merge grammar and the same `Co-authored-by: nancodero <nancodero@proton.me>` trailer in sampled repository history;
- cross-account template leakage in generated repository content.

**Assessment:** the observations support common or closely related repository-generation tooling more strongly than profile similarity alone. They do not establish common human ownership. **[C/H]**

### 2. Earlier August cohort reappears as historical context

A prior August 9–10 follower wave had already exposed six repository owners carrying the same `nancodero` trailer. When revisited on August 27, four of the six previously observed usernames returned HTTP 404 while two remained live.

A 404 is recorded only as loss of public resolution. It does not establish deletion, suspension, rename, or cause.

The two surviving accounts had converged near roughly 1,020 followers, roughly 895 following, and 51–53 repositories, suggesting a possible later lifecycle state. At that point this was only a hypothesis because same-account longitudinal evidence had not yet demonstrated the transition. **[C/H]**

### 3. Major outbound contraction in the August 26 wave

The August 26 accounts later underwent a large outbound contraction from roughly 7,400–7,800 following to approximately 1,329–1,423 following while their repository inventories remained essentially unchanged.

One account, `alberto4442`, was completely enumerated after the contraction:

- following: `1,417`
- followers: `1,556`
- reciprocal relationships: `1,413`
- reciprocal fraction among accounts still followed: `1,413 / 1,417 = 99.7177%`

Rounded: **99.72%**.

This is strong post-event evidence that the retained graph was almost entirely reciprocal. It does **not** prove the pruning algorithm because a complete frozen copy of the pre-pruning following set was not available for direct retained-vs-removed comparison. **[B/C]**

### 4. August 28 five-account generation

Accounts:

- `irenascent`
- `vinamega`
- `RobbyDwk`
- `nahladzulula`
- `cahcacah`

These accounts exposed 60–61 repositories and reproduced the same merge grammar and `nancodero` trailer. Repository naming rounds such as `Yarn*`, `Zen*`, and `Zephyr*` were interleaved across owner namespaces instead of completing one owner at a time.

Five representative immutable Git commits were rechecked on 2026-09-06. All five still resolve publicly and preserve the exact message structure:

```text
Merged PR #1

Automatically merged pull request #1

Co-authored-by: nancodero <nancodero@proton.me>
```

Public anchors:

- `irenascent/ZephyrYarn` — `9404ead160e4f2434656d9f08e237780941be9f8`  
  https://github.com/irenascent/ZephyrYarn/commit/9404ead160e4f2434656d9f08e237780941be9f8
- `vinamega/ZephyrState` — `09d7f0d586e0afb66f0bf089a841a18361b5ad1f`  
  https://github.com/vinamega/ZephyrState/commit/09d7f0d586e0afb66f0bf089a841a18361b5ad1f
- `RobbyDwk/ZephyrRift` — `6a01a7c5bff62c03e395f757ebf8ba1de4275f35`  
  https://github.com/RobbyDwk/ZephyrRift/commit/6a01a7c5bff62c03e395f757ebf8ba1de4275f35
- `nahladzulula/ZephyrQuill` — `c66dfd255a812f1cf4d8c5a3378aa1f6a6c7667b`  
  https://github.com/nahladzulula/ZephyrQuill/commit/c66dfd255a812f1cf4d8c5a3378aa1f6a6c7667b
- `cahcacah/ZephyrIris` — `492860a52c17bb7547993ba89a1e714877c741dd`  
  https://github.com/cahcacah/ZephyrIris/commit/492860a52c17bb7547993ba89a1e714877c741dd

These anchors are especially useful because they do not depend on a mutable profile page. **[A]**

### 5. Repository generation preceded large-scale social growth

The August 28 accounts initially had only 16–18 followers and approximately 637–843 following while their repositories were already populated. Their outbound-following counts then expanded toward roughly 7,700 and their follower counts increased by hundreds while repository inventories remained fixed.

Observed order:

```text
repository generation
        -> portfolio reaches stable state
        -> large outbound-follow expansion
        -> follower acquisition
```

This sequencing supports a phased account-development workflow rather than a static account template. **[C/H]**

### 6. Coordinated entry into the observer's follower set

Immediately before one event, the observer's complete public follower set contained 110 accounts. The next complete collection contained 115. The five additions were exactly the five August 28 accounts.

A later six-account generation produced another complete set difference:

```text
111 followers -> 117 followers
```

The six additions were exactly the six technically linked accounts in that generation.

These are set differences, not inferred follow-event timestamps. GitHub does not publicly expose the exact timestamp at which an account followed another account. **[B/C]**

### 7. Six-account generation with synchronized repository expansion

A later generation contained:

- `emilybarru`
- `lgomesappj`
- `minseochoj`
- `harutosati`
- `whitakeroliver`
- `amurrayeqc`

The accounts initially exposed roughly 11–12 repositories each. Each then gained exactly 67 public repositories, ending at 78–79 repositories. Across those owners, 466 exact-trailer merge commits were recovered across 466 repositories.

Their social phase then moved toward roughly 613–627 followers and roughly 7,600 following while repository inventories remained stable. The same six accounts subsequently entered the observer's follower set together. **[C]**

### 8. September 4 generation

A September 4 generation contained 13 accounts. Twelve exposed 17 repositories and one exposed 16. Owner-scoped searches recovered 219 exact-trailer merge commits across 219 repositories.

The observed production window ran from approximately:

```text
2026-09-04 13:57:27 UTC
through
2026-09-04 18:02:54 UTC
```

Repository production again occurred across multiple owner namespaces during the same bounded period rather than as isolated owner-by-owner activity. **[C]**

### 9. Cross-generation social-graph bridge

Follower sets were successfully collected for eight members of the September 4 generation. Every one contained all five August 28 accounts.

Seven reciprocal following sets were also recovered. Four new owners had the same six-account following set consisting of the five August 28 accounts plus `aibers`.

This is stronger than generic overlap around a high-degree follow-back hub because the five August 28 accounts had already been linked to the repository-generation workflow through Git history before their presence in the newer social graphs was evaluated.

The result creates a cross-generation bridge using two different evidence classes:

```text
Git history + social graph
```

**[C/H]**

## Claim ledger

| Claim | Status | Basis |
|---|---|---|
| Multiple generations share a common or closely related repository-generation workflow | **Strongly supported** | repeated exact trailer, merge grammar, repository morphology, interleaved chronology, public immutable Git anchors |
| Mass following and reciprocal relationships materially contribute to social growth in at least some measured accounts | **Strongly supported for measured accounts** | outbound expansion plus post-pruning `1,413/1,417` reciprocal measurement |
| The workflow has distinct repository-generation, social-acquisition, and pruning phases | **Supported working model** | repeated longitudinal order across multiple generations |
| Reciprocal relationships are preferentially retained during pruning | **Unresolved hypothesis** | 99.72% post-pruning reciprocity is consistent with it, but no complete pre-pruning set was frozen for the measured account |
| One human controls all observed accounts | **Not established** | no credential, network, or operator evidence |
| `nancodero` identifies the operator | **Not established** | trailer is a technical artifact, not verified attribution |
| A specific vendor, service, or account farm is responsible | **Not established** | no sufficient service-level attribution evidence |
| The observer is individually targeted | **Not established** | evidence is consistent with the observer being one member of a reusable target population |
| Disappearing accounts were suspended by GitHub | **Not established** | HTTP 404 has multiple possible causes |

## Disconfirmation and competing explanations

The working interpretation has to survive several weaker explanations:

1. **Shared scaffolding alone.** Common templates can explain identical boilerplate and exact file reuse. They do not by themselves explain repeated follower-wave entry, synchronized social expansion, pruning, and cross-generation graph seeding.
2. **Independent follow-for-follow behavior.** High-degree accounts can naturally share many neighbors. This is why generic hub overlap is treated as weak unless the overlapping accounts were independently linked by Git artifacts first.
3. **Profile imitation.** Bios, avatars, names, and locations are cheap to copy and are not load-bearing evidence here.
4. **Pruning inference.** The 99.72% post-event reciprocal fraction is not promoted into a proven pruning rule without a pre-event complete following set.
5. **Attribution leakage.** Displayed names, commit identities, email strings, and domains are treated as artifacts unless independently tied to a real operator.

## Strongest next experiment

Before another mature account contracts its following list, freeze a complete public baseline containing:

- GitHub numeric account ID;
- login;
- UTC collection timestamp;
- follower count;
- following count;
- complete follower numeric-ID set;
- complete following numeric-ID set;
- repository inventory.

After contraction, collect the same state again.

Then partition the original following set into:

```text
retained relationships
removed relationships
```

and test whether reciprocal relationships were disproportionately retained.

A positive result would move the current post-event clue toward direct behavioral evidence of the pruning mechanism. A negative result would weaken that hypothesis. Either outcome is evidentially useful.

## Verification boundary

The five immutable Git anchors above are public and independently resolvable. Other longitudinal values in this update derive from bounded public-state collections summarized in the published article. Raw API captures, complete relationship membership lists, and private workflow artifacts are not being added to this public package merely to increase exposure.

The original release's sanitization and attribution rules in `NOTICE.md` continue to apply.
