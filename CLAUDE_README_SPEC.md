OPERATOR DIRECTIVE

Read this entire specification before editing any file.

Do not begin implementation after reading only the first sections.

Treat this document as the authoritative specification for the project.

Create an internal implementation plan before making any modifications.

Whenever a conflict exists between an implementation decision and this specification, this specification takes precedence.

Complete the work autonomously whenever possible.

Only interrupt execution if blocked by missing information that cannot be reasonably inferred.

Do not optimize for speed.

Optimize for quality.

The goal is to produce a GitHub profile that feels intentionally crafted, technically mature, visually cohesive and authentic.

# CLAUDE_README_SPEC.md

# GitHub Landing Page — Implementation Specification

Version: 1.0

Repository:
eduardogade

Primary Target:
README.md

---

# Mission

Your objective is to transform the existing GitHub Landing Page into a polished, professional, technically accurate, recruiter-oriented and visually consistent landing page while preserving its existing visual identity, branding and overall philosophy.

This is NOT a redesign project.

This is an implementation, completion and refinement project.

The README already contains a large amount of custom work, including:

- custom section headers;
- custom icons;
- custom HTML;
- layout hacks around GitHub limitations;
- personal branding;
- carefully selected color palette;
- hosted assets.

Your responsibility is to understand the existing implementation before modifying it.

Never replace existing work simply because you would have designed it differently.

---

# Philosophy

Treat this repository exactly as you would treat a production software project.

The README is not documentation.

It is the landing page of a senior engineer.

Every modification should improve one or more of the following:

- readability
- navigation
- consistency
- professionalism
- visual quality
- recruiter experience
- maintainability

Never optimize one of these by significantly hurting another.

---

# Repository Understanding

Before modifying any file, completely understand:

- README.md
- CV.yaml

and every local asset referenced by README.md.

Whenever README references hosted assets, inspect those resources as well.

Those assets define the existing visual language and must remain consistent throughout the project.

---

# Source of Truth

The following priority order is mandatory.

1. README.md layout and branding
2. CV.yaml (career information)
3. Existing repositories
4. Existing website assets
5. Existing GitHub profile
6. Public repositories
7. External references

Whenever conflicts occur, report them instead of silently choosing one.

---

# Non-Negotiable Constraints

Never redesign the landing page.

Never change the branding.

Never change the color palette.

Never replace custom section headers.

Never replace the visual identity.

Never simplify the page simply because minimalism is fashionable.

The owner explicitly prefers a rich, highly informative, carefully organized landing page.

Whenever additional content is introduced, it must integrate naturally into the existing design language.

---

# Creative Freedom

You are encouraged to make autonomous decisions whenever multiple good solutions exist.

However, every decision must preserve:

- branding
- consistency
- tone
- layout philosophy

When content is missing, do not leave the section empty.

Instead:

- write professional placeholder content;
- generate high-quality draft content;
- generate TODO prompts when creative writing is impossible;
- report remaining manual work in the final report.

The objective is to make the repository feel finished.

---

# HTML Philosophy

GitHub HTML support is limited.

The existing README already contains numerous workarounds.

Preserve them.

Whenever introducing new HTML:

- prefer GitHub-supported HTML;
- avoid CSS-dependent solutions;
- avoid JavaScript;
- avoid unsupported HTML attributes;
- prefer semantic HTML;
- maintain graceful degradation.

Never introduce rendering that depends on unsupported GitHub behavior.

---

# Browser Validation

Rendering correctness is mandatory.

After every significant visual modification:

- render the README;
- inspect it in the browser;
- verify alignment;
- verify spacing;
- verify image sizing;
- verify responsiveness;
- verify dark/light theme behavior whenever possible.

If something renders incorrectly:

fix it.

Do not simply report it.

---

# Existing Design Language

Before creating any new visual element, infer the existing design language.

Examples include:

- section headers
- spacing
- icon sizes
- cards
- tables
- alignment
- typography
- expandable sections
- separators

Every newly created component should appear as if it had originally been part of the project.

---

# Consistency Rules

Throughout the entire README maintain consistent:

- spacing
- indentation
- HTML formatting
- Markdown formatting
- heading hierarchy
- icon style
- emoji usage
- capitalization
- terminology
- card layout
- table formatting

If inconsistencies already exist, normalize them whenever safe.

---

# Working Methodology

Do not edit randomly.

Instead follow this workflow.

1.

Understand the repository.

↓

2.

Understand the README.

↓

3.

Understand the visual language.

↓

4.

Understand CV.yaml.

↓

5.

Create an internal implementation plan.

↓

6.

Execute section by section.

↓

7.

Validate rendering.

↓

8.

Repeat.

↓

9.

Perform global consistency review.

↓

10.

Produce final report.

---

# Internal TODO List

Create and maintain your own implementation checklist.

Keep it updated during execution.

The checklist is for your own reasoning.

Do not ask the user to create one.

---

# Quality Standard

Whenever you are unsure between two implementations, prefer the one that would most likely appear in the GitHub profile of a Principal Engineer, Distinguished Engineer or Technical Fellow.

Avoid flashy elements.

Avoid unnecessary animations.

Avoid gimmicks.

Aim for elegance, polish and longevity.

---

# Deliverable

When the task is complete, README.md should feel like a cohesive, professionally engineered landing page rather than a collection of independent sections written over time.

Subsequent sections of this specification describe each README section individually and define their acceptance criteria.

---

# SECTION IMPLEMENTATION SPECIFICATION (PART 1)

This section specifies the implementation requirements for Sections 0 through 6.

The implementation order defined here is intentional.

Complete every section before proceeding to the next.

Whenever a section is marked as "Done", it still requires validation and refinement.

---

# SECTION 0 — HEADER

Status:
Implemented

Objective:

Preserve the existing implementation.

Do not redesign.

Do not simplify.

Do not modify branding.

---

## Tasks

- Verify that all images render correctly.
- Verify SVGs.
- Verify spacing.
- Verify responsiveness.
- Verify links.
- Verify typing animation (if present).
- Verify badges.
- Verify dark/light theme compatibility whenever possible.

---

## Acceptance Criteria

The Header remains visually identical or objectively improved while preserving its current identity.

No redesign.

---

# SECTION 1 — PROFILE

Status:
Mostly complete.

Objective:

Keep the current section.

Only improve technical quality.

---

## Tasks

Review:

- wording
- grammar
- consistency
- hyperlinks
- formatting

Remove only links that are:

- broken
- deprecated
- duplicated

Do NOT remove content simply because it appears excessive.

Preserve the existing "Data Platform Engineer" positioning.

---

## Acceptance Criteria

The section communicates the author's professional identity more clearly while preserving the existing style.

---

# SECTION 2 — CAREER

Status:
Mostly complete.

Objective:

Preserve existing content.

Improve wording only when beneficial.

---

## Ordering Decision

Evaluate whether the following order produces a better recruiter experience:

Header

↓

Profile

↓

Contact

↓

Pinned Repositories

↓

Career

↓

Remaining Sections

If this ordering is clearly superior, apply it.

Otherwise preserve the existing order.

---

## Text

Improve only:

- clarity
- grammar
- fluency
- readability

Do not reduce personality.

Do not remove achievements.

Do not reduce confidence.

The tone should remain ambitious while staying professional.

---

## Acceptance Criteria

The section should read naturally while maintaining its intended impact.

---

# SECTION 3 — CV

Status:
Implemented

Important:

CV.yaml is the authoritative source.

README is only a presentation layer.

---

## Tasks

Compare:

README.md

vs

CV.yaml

Synchronize:

- dates
- titles
- institutions
- positions
- descriptions
- technologies
- awards
- publications
- responsibilities

Whenever wording can be improved while preserving meaning, rewrite it.

Whenever README omits relevant information present in CV.yaml, include it if appropriate.

Do not invent information.

---

## Acceptance Criteria

README accurately reflects CV.yaml while being considerably more readable.

---

# SECTION 4 — CONTACT

Status:
Mostly complete.

---

## Tasks

Validate every external link.

For every broken link:

- do not silently replace it;
- include it in the final report.

Verify:

- GitHub
- LinkedIn
- Medium
- personal website
- email
- every social link

Inspect the subsection:

Details

Correct all self-referencing links.

Normalize formatting if necessary.

The business card image will be updated manually by the repository owner.

Do not modify it.

---

## Acceptance Criteria

Every reachable link works.

Broken links appear in the final report.

---

# SECTION 5 — PINNED REPOSITORIES

Status:
Not implemented.

This section is extremely important.

Treat it as one of the primary recruiter-facing sections.

---

## General Goal

Create visually attractive repository cards while remaining compatible with GitHub Markdown rendering.

Reuse the visual language already established throughout the README.

---

# Upper Section

Display only:

1.

Apollo

2.

Blacksmith

3.

Olympus

Prefer HTML when appropriate.

Markdown is acceptable if it produces a cleaner result.

Each repository should appear as an individual card.

Each card should contain:

- centered repository image
- repository title
- concise description
- repository link

Use the current GitHub repository description as temporary text.

Do not invent descriptions.

---

## Card Layout

The visual appearance should resemble professional portfolio cards.

Maintain:

- equal spacing
- equal dimensions
- consistent typography

---

# Expandable Section

Inside the existing <details> block create repository cards for:

- Apollo
- Blacksmith
- Olympus
- Bloom
- Musique
- Wildlife
- Fabric
- Uqbar
- GusmaoLab

Maintain the exact same card style.

---

## Images

Whenever repository preview images already exist, use them.

Otherwise:

create clean placeholders.

Report missing images.

---

## Acceptance Criteria

The repository section should immediately communicate the breadth and quality of the author's work.

---

# SECTION 6 — CONTRIBUTIONS

Status:
Not implemented.

Creative freedom is encouraged.

---

## Objective

Demonstrate meaningful contributions without relying solely on GitHub's default contribution graph.

Avoid redundant information.

Avoid decorative widgets that add no informational value.

---

## Suggested Content

Examples include:

- Open Source Contributions
- Community Impact
- Maintainer Activities
- Research Collaborations
- External Organizations
- Pull Requests
- Technical Mentorship

Choose only what can be supported with publicly observable evidence.

---

## If insufficient information exists

Create a tasteful placeholder.

Do not leave the section empty.

The placeholder should appear intentional rather than unfinished.

Example themes:

- "Work in Progress"
- "More Contributions Coming"
- "Currently Curating Public Contributions"

Do NOT use wording that suggests abandonment.

---

## Acceptance Criteria

The section should reinforce technical credibility without duplicating information already present elsewhere in the README.

---

# SECTION IMPLEMENTATION SPECIFICATION (PART 2)

This section specifies the implementation requirements for Sections 7 through 12.

Continue following every global rule established in Part 1.

Maintain visual consistency with every previously implemented section.

Whenever a new reusable component is created (cards, tables, layouts, placeholders, etc.), reuse it consistently throughout the remainder of the README.

---

# SECTION 7 — GITHUB STATISTICS

Status:
Partially planned.

Objective:

Present GitHub statistics that genuinely help recruiters understand the author's engineering activity.

Avoid decorative widgets whose only purpose is visual appeal.

The section should feel analytical rather than playful.

---

## Upper Section

Create a concise dashboard using high-quality GitHub statistics.

Examples include:

- GitHub Stats
- Contribution Calendar
- Streak Statistics
- Contribution Graph
- Repository Statistics

Evaluate available public providers.

Prefer actively maintained services.

Avoid abandoned projects.

---

## Contribution Graph

Historically the author preferred 3D contribution graphs because they communicate activity better than normalized color heatmaps.

Investigate current options.

If they still produce high-quality results:

include one.

Otherwise:

recommend against using them and explain why in the final report.

---

## Expandable Section

Inside the existing <details> section include additional statistics such as:

- languages
- repositories
- commits
- stars
- pull requests
- issues
- contribution distribution

Only include information that adds value.

Do not repeat statistics already visible above.

---

## Quality Requirements

The section should communicate engineering activity rather than simply displaying colorful widgets.

Every widget should answer a question a recruiter might reasonably have.

---

## Acceptance Criteria

A technically inclined recruiter should gain a better understanding of the author's engineering profile after reading this section.

---

# SECTION 8 — GITHUB ANALYTICS

Status:
Concept only.

Objective:

Determine whether this section provides information that is sufficiently different from "GitHub Statistics".

---

## Investigation

Research whether meaningful analytics exist for topics such as:

- impact across repositories
- external contributions
- repository influence
- dependency relationships
- collaboration metrics
- review activity
- community engagement

If high-quality analytics exist:

implement the section.

Otherwise:

remove this section entirely.

---

## Removal Policy

If removed:

replace it with a tasteful placeholder explaining that the section is reserved for future analytics once suitable public metrics become available.

The placeholder should feel intentional.

Never leave empty space.

---

## Acceptance Criteria

Either:

a useful analytics section exists,

or

the section has been intentionally deferred.

Never produce a weak section merely to preserve the original outline.

---

# SECTION 9 — TECHNOLOGY STACK

Status:
Upper section implemented.

Expandable section missing.

---

## Upper Section

Review existing implementation.

Synchronize technologies with CV.yaml whenever appropriate.

Do not redesign the existing visual language.

---

## Expandable Section

Generate the complete technology inventory.

The authoritative source is:

CV.yaml

Search for every technology mentioned.

Whenever icons are already used elsewhere in the README, preserve the same style.

Search known icon providers for missing technologies.

Examples include:

- Devicon
- Simple Icons
- Shields.io
- SVG repositories

Maintain visual consistency.

---

## Missing Icons

If an icon cannot be located:

do not invent one.

Instead:

append it to the final report.

Include:

- technology
- suggested icon source (if known)

---

## Organization

Group technologies into meaningful categories.

For example:

Data Engineering

Cloud

Infrastructure

Programming Languages

Databases

Machine Learning

DevOps

Observability

Architecture

Scientific Computing

Documentation

Avoid one giant unordered list.

---

## Acceptance Criteria

The section should represent the author's complete technical toolbox while remaining visually organized.

---

# SECTION 10 — RESEARCH

Status:
Implemented.

---

## Tasks

Perform a consistency review only.

Check:

- formatting
- wording
- grammar
- hyperlinks
- spacing
- consistency with the remainder of the README

No redesign.

No additional content unless clearly beneficial.

---

## Acceptance Criteria

Research remains visually and stylistically aligned with the rest of the landing page.

---

# SECTION 11 — WRITING & COMMUNICATION

Status:
Partially implemented.

---

## Upper Section

Create four highlighted links.

Use the following destinations.

Blog

Temporary URL:

https://www.gusmaolab.org

Atlas Learning Series

Temporary URL:

https://www.gusmaolab.org

Medium

Reuse the existing Medium link already present inside README.md.

Book

Reuse the existing book link already present inside README.md.

Do not invent URLs.

---

## Expandable Section

Write approximately three paragraphs.

Theme:

Writing clearly.

Topics include:

- technical communication
- documentation
- architecture writing
- explaining complex systems
- communicating across engineering teams
- transforming complexity into clarity

The tone should be thoughtful and professional.

Avoid clichés.

Avoid AI-like prose.

---

## Acceptance Criteria

Readers should understand that written communication is treated as an engineering skill rather than an auxiliary skill.

---

# SECTION 12 — AVAILABILITY

Status:
Not implemented.

Objective:

Communicate professional availability in a confident, respectful and recruiter-friendly manner.

---

## Upper Section

Summarize availability.

Include:

- open to work
- remote
- hybrid
- on-site
- Europe
- Brazil
- relocation
- worldwide opportunities

Express geographical preference approximately as:

Europe

↓

Brazil

↓

Worldwide

Without sounding restrictive.

---

## Expandable Section

Write a more complete explanation.

Topics should include:

- preferred work style
- engineering philosophy
- long-term thinking
- software craftsmanship
- sustainable engineering
- collaboration
- architecture
- code quality

Convey clearly that:

The objective is producing high-quality engineering rather than maximizing delivery speed.

Avoid wording that could be interpreted as arrogance.

Avoid negative statements regarding employers, technologies or operating systems.

Instead of criticizing specific vendors or platforms, emphasize that productivity is highest in environments that provide robust developer tooling, reproducibility, automation and efficient workflows.

Focus on positive preferences rather than negative comparisons.

---

## Acceptance Criteria

A hiring manager should understand:

- where the author is available;
- how he prefers to work;
- what engineering values he brings to a team.

The section should increase hiring confidence rather than create unnecessary controversy.

---

# SECTION IMPLEMENTATION SPECIFICATION (PART 3)

This section specifies the implementation requirements for Sections 13 through 18.

These sections are considerably more personal than previous ones.

Maintain professionalism while preserving the author's personality.

Do not make the README feel corporate.

The objective is to make it feel human, thoughtful and memorable.

---

# SECTION 13 — ROADMAP

Status:
Concept defined.

Objective:

Present where the author's engineering journey is heading rather than listing a TODO list.

This section represents long-term technical direction.

---

## Upper Section

Insert a centered placeholder image.

Requirements:

- completely black
- simple placeholder
- approximately half-page width
- maintain current visual language

The image will be replaced later.

---

## Expandable Section

Insert a larger placeholder image.

Requirements:

- centered
- same visual style
- larger dimensions

The image will eventually become a roadmap illustration.

---

## Placeholder Text

Write a concise explanation describing that this section will eventually present:

- long-term technical goals
- research directions
- engineering initiatives
- platform evolution
- open-source roadmap

The wording should make the placeholder appear intentional.

---

## Final Report

Report:

- recommended image dimensions;
- recommended aspect ratio;
- recommended maximum GitHub rendering width.

If multiple sizes are suitable, provide a recommended range.

---

## Acceptance Criteria

The section should already feel integrated into the README despite temporary placeholder artwork.

---

# SECTION 14 — EDUCATION

Status:
Upper section implemented.

---

## Upper Section

Review only.

Synchronize with CV.yaml.

No redesign.

---

## Expandable Section

For each degree create an expandable subsection.

Describe:

- major accomplishments;
- major research themes;
- significant technical achievements;
- important collaborations;
- notable outcomes.

Whenever enough information is unavailable, create clearly identified placeholders.

Do not invent achievements.

---

## Placeholder Style

Use concise placeholders that indicate the expected future content.

Avoid:

"TBD"

Prefer:

"This subsection will summarize..."

---

## Final Report

List every placeholder requiring manual completion.

---

## Acceptance Criteria

The education section should communicate growth rather than merely listing degrees.

---

# SECTION 15 — PHILOSOPHY & ETHICS

Status:
Concept defined.

Objective:

Communicate engineering principles.

Not political opinions.

Not personal ideology.

Not motivational quotes.

This section should strengthen trust.

---

## Upper Section

Produce concise engineering principles.

Topics should include:

- software craftsmanship;
- reproducibility;
- documentation;
- maintainability;
- testing;
- data governance;
- healthcare data responsibility;
- sensitive data handling;
- privacy;
- scientific reproducibility;
- engineering ethics.

Present them as concise bullet points.

---

## Expandable Section

Write approximately three to four thoughtful paragraphs.

Themes include:

- engineering responsibility;
- long-term maintainability;
- readable software;
- scientific integrity;
- reproducible engineering;
- ethical use of machine learning;
- ethical handling of data;
- balancing innovation with responsibility.

The tone should be reflective.

Avoid preaching.

Avoid ideological language.

Avoid polarizing examples.

---

## Intellectual Influences

The author appreciates thinkers such as:

- Ludwig Wittgenstein
- Albert Camus
- Karl Marx

If intellectual influences are mentioned:

focus on ideas that translate naturally into engineering practice.

Examples:

- clarity of language;
- responsibility;
- understanding systems;
- questioning assumptions;
- social impact of technology.

Never produce hero worship.

Never produce political discussion.

The reader should perceive mature engineering values.

---

## Acceptance Criteria

The section should increase credibility while remaining suitable for industry audiences.

---

# SECTION 16 — CAUSES

Status:
Concept defined.

Objective:

Present meaningful causes supported by genuine participation.

Avoid appearing performative.

---

## Upper Section

Create reusable cards.

The same visual language introduced in "Pinned Repositories" should be reused.

If cards cannot be rendered satisfactorily, use concise highlighted panels instead.

Include:

---

### Global Burden of Disease

Role:

Collaborator

Period:

2018–Present

Short description:

Contributing to one of the world's largest collaborative efforts for measuring disease burden through data infrastructure, engineering and scientific collaboration.

---

### TransEmpregos

Role:

Volunteer

Period:

2024–Present

Short description:

Supporting infrastructure and data engineering for employability initiatives focused on transgender professionals.

---

### ABRATA

Role:

Volunteer

Period:

2022–2025

Short description:

Supporting initiatives that improve awareness and education regarding mood disorders and mental health.

---

## Expandable Section

Visit each official website.

Understand their mission.

Write a concise explanation describing:

- why the organization matters;
- its societal impact;
- why readers may wish to know more.

Include links to:

Global Burden of Disease

https://www.healthdata.org/research-analysis/gbd/collaborator-network

TransEmpregos

https://www.transempregos.com.br/

ABRATA

https://www.abrata.org.br/seja-um-voluntario-abrata/

Do not copy text.

Summarize.

---

## Acceptance Criteria

Readers should understand that community involvement reflects long-term commitment rather than résumé decoration.

---

# SECTION 17 — OTHER ACTIVITIES

Status:
Concept defined.

Objective:

Present personal activities without reducing professionalism.

---

## Upper Section

Create one horizontal information card.

Layout:

Left:

placeholder image

Right:

Powerlifting

Placeholder narrative describing the author's journey.

Leave clearly identified placeholders where personal storytelling will later be inserted.

---

## Expandable Section

Reuse the exact same horizontal card design.

Create one card for each topic:

- Open Source Contributor
- Lecturer & Public Speaker
- BioConductor & Cloud Composer
- Writer — Technical & Prose

Use placeholder images.

Use professionally written placeholder content.

Maintain visual consistency across every card.

---

## Final Report

Report suggested dimensions for:

- horizontal images;
- aspect ratios;
- recommended GitHub rendering sizes.

---

## Acceptance Criteria

The section should communicate breadth without distracting from the engineering profile.

---

# SECTION 18 — BLOOM

Status:
Concept defined.

This is the most personal section in the entire README.

Treat it accordingly.

---

## Objective

Write an original piece describing the author's engineering philosophy through the metaphor of Bloom.

Do not imitate any existing work.

Do not quote external texts.

Instead, use them only as inspiration.

---

## Themes

Possible themes include:

- curiosity;
- systems thinking;
- emergence;
- nature;
- trees;
- growth;
- algorithms;
- architecture;
- complexity;
- stochasticity;
- order emerging from chaos;
- elegant software;
- readable code;
- beauty through function;
- sustainable engineering;
- platforms that mature organically.

The metaphor of a tree is particularly encouraged.

Examples:

Roots

Architecture

Branches

Abstractions

Leaves

Features

Bloom

Engineering maturity

The writing should remain subtle.

Avoid becoming mystical.

---

## Style

Aim for thoughtful prose rather than poetry.

The text should feel timeless.

It should communicate values more than biography.

The writing should leave the reader with a memorable impression.

---

## Inspiration

The author particularly appreciates the intersection of:

- nature;
- music;
- mathematics;
- computation;
- scientific discovery;
- software architecture.

Those themes may naturally appear throughout the text.

---

## Acceptance Criteria

The final section should become one of the defining elements of the entire landing page.

It should leave readers with a strong sense of identity while remaining elegant, authentic and professional.

---

# IMPLEMENTATION PROTOCOL, TESTING, REPORTING & ACCEPTANCE CRITERIA

This section defines how the implementation should be executed, validated and delivered.

It is as important as the individual section specifications.

Treat it as the project's Definition of Done.

---

# Autonomous Execution

You are expected to work autonomously.

Avoid interrupting execution whenever a reasonable engineering decision can be made.

If multiple acceptable alternatives exist:

- choose one;
- document the decision in the final report.

Do not stop to ask for stylistic preferences unless they fundamentally change the implementation.

The repository owner explicitly prefers fewer interruptions over constant confirmations.

---

# Iterative Development

Do NOT attempt to modify the entire README in a single pass.

Instead, iterate.

For each iteration:

1. understand the current section;
2. implement improvements;
3. validate rendering;
4. fix rendering problems;
5. continue.

After completing all sections:

perform one complete consistency review across the entire README.

---

# Browser Validation

Rendering validation is mandatory.

Whenever possible:

- render the README using GitHub's renderer;
- inspect it visually;
- verify alignment;
- verify spacing;
- verify image rendering;
- verify expandable sections;
- verify cards;
- verify tables;
- verify responsiveness.

If rendering problems are detected:

fix them before moving forward.

Do not simply report them.

---

# GitHub Compatibility

Always prefer solutions that are:

- officially supported;
- stable;
- unlikely to be deprecated;
- compatible with GitHub's Markdown renderer.

Avoid depending on:

- unsupported HTML;
- unsupported CSS;
- JavaScript;
- browser-specific behavior.

Whenever a workaround is necessary:

prefer the simplest one.

---

# Existing Workarounds

The current README already contains several carefully designed workarounds.

Before replacing any workaround:

understand why it exists.

Never assume something is "ugly" without first verifying whether it exists because of GitHub limitations.

---

# Visual Consistency Review

Before considering the project complete, review the entire README for consistency.

Verify:

- spacing;
- alignment;
- typography;
- section ordering;
- heading hierarchy;
- icon sizes;
- card dimensions;
- table formatting;
- expandable sections;
- image alignment;
- hyperlink formatting.

Normalize inconsistencies whenever safe.

---

# Placeholder Policy

Whenever placeholder content is required:

make it intentional.

Never use:

- TODO
- Lorem Ipsum
- TBD
- Coming Soon

Instead use professional placeholder text explaining what the future content will represent.

The README should always feel intentionally incomplete rather than abandoned.

---

# Creative Writing Policy

Whenever original text is required:

write it.

Avoid AI clichés.

Avoid exaggerated marketing language.

Avoid buzzwords.

Prefer:

- thoughtful;
- technically mature;
- timeless;
- concise;
- readable.

When uncertainty exists regarding personal details:

write high-quality draft content that can later be edited by the repository owner.

If doing so would require inventing facts:

create a clearly identified placeholder instead.

---

# Image Policy

Whenever images are introduced:

report:

- recommended dimensions;
- recommended aspect ratio;
- suggested maximum rendering width;
- suggested file format.

Whenever placeholders are used:

make them visually consistent.

Use solid black placeholder images unless another placeholder style integrates better with the existing branding.

---

# External Resources

You may inspect:

- existing repositories;
- GitHub profile;
- linked websites;
- referenced assets;
- public documentation;
- icon providers.

Whenever useful inspiration is found:

adapt the idea.

Never copy another person's README.

The objective is originality.

---

# Rendering Suggestions

Suggestions beyond the requested implementation are encouraged.

Examples:

- improved layouts;
- reusable components;
- dynamic headers;
- SVG improvements;
- rendering tricks compatible with GitHub;
- maintainability improvements.

Do not implement speculative ideas unless they clearly improve the project.

Instead, include them in the final report.

---

# Future Compatibility

Whenever multiple implementation choices exist:

prefer the solution most likely to remain compatible with future GitHub rendering behavior.

Avoid techniques that already appear deprecated or unstable.

If uncertainty exists:

mention it in the final report.

---

# Things That Must Never Be Lost

Throughout the implementation preserve:

- personality;
- ambition;
- authenticity;
- technical credibility;
- curiosity;
- elegance;
- craftsmanship.

This README should feel like it belongs to a thoughtful engineer, not a corporate template.

---

# Final Report

Produce a comprehensive implementation report.

The report should be concise but complete.

Organize it using the following structure.

---

# Executive Summary

Briefly summarize:

- what was implemented;
- overall quality improvements;
- major architectural decisions.

---

# Completed Work

List every completed task grouped by README section.

---

# Manual Actions Still Required

List every remaining manual task.

Examples:

- placeholder images;
- personal stories;
- photos;
- creative decisions;
- unavailable information.

---

# Broken Links

List every broken or unreachable link discovered.

---

# Missing Icons

List technologies whose icons could not be located.

Include suggested icon providers whenever possible.

---

# Placeholder Images

List every placeholder image inserted.

For each image report:

- location;
- suggested dimensions;
- aspect ratio;
- recommended replacement strategy.

---

# Rendering Limitations

Describe GitHub limitations encountered.

Explain any workaround that had to be used.

---

# Recommendations

List optional improvements that were intentionally not implemented.

Examples:

- alternative layouts;
- reusable components;
- dynamic SVGs;
- rendering enhancements;
- future automation opportunities.

---

# Creative Writing Suggestions

Whenever placeholder text remains:

provide high-quality prompts that could later be used to generate the final content.

Each prompt should be fully self-contained.

---

# Future Improvements

Provide a prioritized list.

Classify each item as:

High

Medium

Low

according to expected impact.

---

# Acceptance Checklist

Before declaring completion verify that ALL of the following are true.

□ README renders correctly.

□ Links were validated.

□ Visual identity was preserved.

□ Branding remained consistent.

□ CV.yaml was synchronized.

□ Section ordering was reviewed.

□ Cards render correctly.

□ Expandable sections work.

□ Images are aligned.

□ Placeholder content is intentional.

□ Final report was generated.

□ Remaining manual tasks were documented.

Only declare success after every applicable item has been verified.

---

# Success Definition

The project is considered complete when:

- the README appears professionally finished;
- the visual identity remains unmistakably the author's;
- recruiters can navigate it naturally;
- technical readers can quickly assess the author's expertise;
- every implemented section feels cohesive with the rest of the landing page;
- remaining unfinished work is intentional, documented and easy to complete later.

At completion, the repository should feel like a mature engineering portfolio rather than a work-in-progress.

End of specification.
