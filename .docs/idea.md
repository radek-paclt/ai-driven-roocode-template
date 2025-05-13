### 💡 Návrh řešení: Orchestrovaný AI vývoj s důrazem na TDD, interní pamětí projektu, škálovatelností a lidským dohledem – Verze 8 (Finální)

**Hlavní vize:** Vytvořit systém pro vývoj softwaru řízený AI agenty (specializovanými Roo Code módy), který je postaven na metodologii SPARC, agilních principech a Test-Driven Development (TDD). Systém klade důraz na **obousměrnou komunikaci a porozumění mezi AI Architektem a Business Vlastníkem (BV)**, využívá **flexibilní a konfigurovatelnou strukturu interních pracovních dokumentů v adresáři `.project-memory/`** jako perzistentní paměť projektu, implementuje **robustní mechanismy pro řešení konfliktů**, a zajišťuje smysluplný lidský dohled. Verzování pomocí Gitu a Semantic Commits je klíčové pro sledovatelnost a správu. Adresář `docs/` bude vyhrazen pro finální, publikovatelnou dokumentaci projektu.

---

**Kapitola 1: Základní stavební kameny**

*   **1.1 Metodologie SPARC jako orchestrační rámec**:
    *   **S**pecification: Detailní definice požadavků a cílů.
    *   **P**seudocode: Návrh logiky a TDD kotev.
    *   **A**rchitecture: Návrh škálovatelné a modulární systémové architektury.
    *   **R**efinement: Implementace (kódování, TDD, ladění, bezpečnostní revize, optimalizace).
    *   **C**ompletion: Integrace, finální dokumentace, nasazení a monitoring.
*   **1.2 AI Agenti (Roo Code Custom Modes)**:
    *   Každý agent má specifickou roli (slug, name, roleDefinition, customInstructions) a oprávnění (groups).
    *   Agenti jsou aktivováni a koordinováni `SPARC Orchestratorem`.
*   **1.3 Klíčoví SPARC Agenti (počáteční sada)**:
    1.  **⚡️ SPARC Orchestrator (`sparc`)**: Hlavní koordinátor, deleguje úkoly pomocí `new_task`, spravuje tok práce, spravuje verzování interní dokumentace v `.project-memory/` pomocí Gitu.
    2.  **📋 Specification Writer (`spec-pseudocode`)**: Transformuje business požadavky na detailní specifikace a pseudokód (ukládá do `.project-memory/`), úzce spolupracuje s BV (skrze Orchestrátora) a `tdd` agentem.
    3.  **🏗️ Architect (`architect`)**: Navrhuje systémovou architekturu, datové modely, API (ukládá do `.project-memory/`); aktivně komunikuje a vysvětluje návrhy BV.
    4.  **🧠 Auto-Coder (`code`)**: Implementuje kód na základě specifikací a testů.
    5.  **🧪 Tester (TDD) (`tdd`)**: Píše testy *před* implementačním kódem na základě specifikací.
    6.  **📚 Documentation Writer (`docs-writer`)**: Generuje a udržuje **finální** projektovou dokumentaci v adresáři `docs/` na základě artefaktů z `.project-memory/` a kódu.
    7.  **🛡️ Security Reviewer (`security-review`)**: Provádí bezpečnostní audity.
    8.  **(Volitelný) 🤝 Mediator Agent**: Specializovaný agent pro pomoc při řešení konfliktů mezi jinými agenty.
    *   Další agenti (Debug, DevOps, Integration, Optimizer, Monitor, Ask, Tutorial) mohou být přidáni později dle potřeby.
*   **1.4 Projektové Postuláty**:
    *   Sada neměnných základních pravidel, která musí dodržovat všichni AI agenti.
    *   Uloženy v `.project-memory/project_postulates.md`.

---

**Kapitola 2: Komunikace a delegace – `new_task` a `attempt_completion`**

*   **2.1 `new_task` – Anatomie delegace**:
    *   Strukturovaná `message` JSON zpráva.
    *   **Klíčové atributy `message`**:
        *   `taskId`, `parentTaskId`, `delegatedToMode`
        *   `objective`
        *   `context` (sumarizace z MCP/Summarizeru)
        *   `inputs`: Seznam vstupních artefaktů (odkazy směřují primárně do `.project-memory/` a jsou verzovány).
        *   `expectedOutputs`: Popis očekávaných výstupních artefaktů (ukládají se primárně do `.project-memory/` a jsou verzovány).
        *   `constraintsAndRules`, `acceptanceCriteria`, `priority`, `deadlineHint`.
*   **2.2 `attempt_completion` – Hlášení o dokončení**:
    *   Strukturovaná zpráva od agenta k Orchestrátorovi.
    *   **Klíčové atributy**: `taskId`, `result` ("success", "failure", "clarification_needed", "conflict_detected"), `summary`, `outputArtifacts` (odkazy na verze v Gitu v `.project-memory/`), `issues_encountered`.

---

**Kapitola 3: Interní paměť projektu (".project-memory/") – Flexibilní a konfigurovatelná struktura**

*   **3.1 Koncept**:
    *   Adresář `.project-memory/` v kořeni projektu slouží jako primární, strukturovaná, **interní pracovní paměť projektu** pro AI agenty. Není určen pro přímou konzumaci koncovými uživateli projektu.
    *   Obsahuje Markdown soubory a diagramy (např. Mermaid).
    *   Je **verzoatelná pomocí Gitu**, Orchestrátor je zodpovědný za commity (Semantic Commits).
    *   Slouží jako "single source of truth" pro AI agenty a interní lidský dohled (vývojový tým).
    *   Struktura je modulární a konfigurovatelná.
*   **3.2 Obecné principy pro MD soubory v `.project-memory/`**:
    *   **3.2.1 Konzistentní pojmenování**: `snake_case_with_prefixes.md`, číselné prefixy.
    *   **3.2.2 Standardní Markdown syntaxe**.
    *   **3.2.3 Metadata/Frontmatter (povinné)**:
        ```yaml
        ---
        title: "Název dokumentu vystihující obsah"
        version: "major.minor.patch"
        status: "Draft | InReview | ApprovedByBV | ApprovedByTechLead | Implemented | Obsolete"
        created_by: "ID Agenta nebo 'BusinessOwner' nebo 'SPARC_Orchestrator'"
        created_date: "YYYY-MM-DDTHH:MM:SSZ"
        last_modified_by: "ID Agenta nebo 'SPARC_Orchestrator'"
        last_modified_date: "YYYY-MM-DDTHH:MM:SSZ"
        related_tasks: ["TASK-ID-001", "FEATURE-XYZ"]
        relevant_links: ["./02_related_document.md"]
        tags: ["architektura", "iot", "backend"]
        parent_document: "./relative/path/to/parent_doc.md"
        child_documents: ["./details/specific_module_spec.md"]
        related_concepts: ["concept_id_1", "glossary_term_X"]
        project_type_tags: ["web-app", "api-backend"]
        visibility: "internal" # Označení, že jde o interní pracovní dokument
        ---
        ```
    *   **3.2.4 Sekce pro AI agenty (volitelné)**.
    *   **3.2.5 Odkazování mezi soubory**: Relativní cesty v rámci `.project-memory/`.
*   **3.3 Modulární a konfigurovatelná struktura adresáře `.project-memory/`**:
    *   **3.3.1 Základní ("Core") struktura (neměnná)**:
        ```
        .project-memory/
        ├── project_meta/
        │   ├── documentation_structure_config.md
        │   └── project_glossary.md
        ├── idea_clarification/ # Dříve idea/
        │   ├── 01_initial_idea_capture.md
        │   ├── 02_architect_clarification_log.md
        │   ├── 03_architectural_explanations_for_bv.md
        │   ├── 04_refined_idea_and_scope.md
        │   └── bv_architect_sync_log.md
        ├── project_context/
        │   ├── product_overview.md
        │   ├── active_threads.md
        │   ├── decision_log.md
        │   ├── system_patterns.md
        │   ├── progress_tracker.md
        │   └── conflict_resolution_log.md
        └── project_postulates.md
        ```
    *   **3.3.2 Volitelné moduly/adresáře**: Orchestrátor vybírá šablonu nebo dynamicky přizpůsobuje. Příklady: `hld/`, `lld/`, `api_design_artifacts/`, `ui_ux_working_docs/`, `testing_strategy_and_plans/`, `coding_guidelines_and_notes/`. Změny logovány v `documentation_structure_config.md`.
*   **3.4 Správa paměti a verzování**: Orchestrátor spravuje zápisy a commity do Gitu.
*   **3.5 To-Do Listy (`todo_*.md`)**: Umístěny v relevantních podadresářích `.project-memory/`.

---

**Kapitola 4: Geneze projektu: Obousměrné vyjasňování a návrh HLD**

*   **4.1 Zachycení myšlenky BV**: Chat -> Orchestrátor/`ask` agent zaznamená do `.project-memory/idea_clarification/01_initial_idea_capture.md`.
*   **4.2 Počáteční zpracování Orchestratorem**: Analýza, konfigurace dokumentační struktury v `.project-memory/project_meta/documentation_structure_config.md`, příprava úkolu pro `architect`.
*   **4.3 Angažmá `Architect` agenta: Iterativní vyjasňování A ZPĚTNÉ VYSVĚTLOVÁNÍ**:
    1.  **Kritická revize a dotazy Architekta**: Generuje otázky (ukládá do `.project-memory/idea_clarification/architect_questions_batch_N.md`).
    2.  **Facilitace Orchestratorem (BV -> Architekt)**: Orchestrátor sbírá odpovědi od BV, zaznamenává do `.project-memory/idea_clarification/02_architect_clarification_log.md`.
    3.  **Fáze zpětného vysvětlování (Architekt -> BV)**:
        *   `Architect` agent vytváří/aktualizuje `.project-memory/idea_clarification/03_architectural_explanations_for_bv.md`.
        *   Orchestrátor prezentuje BV.
    4.  **BV Revize a Zpětná vazba**: Zaznamenává Orchestrátor do `.project-memory/idea_clarification/bv_architect_sync_log.md`.
    5.  **Iterace**: Cyklus se opakuje. `.project-memory/idea_clarification/04_refined_idea_and_scope.md` je finálně schválen BV.
*   **4.4 Formulace HLD `Architect` agentem**: Vytváří HLD artefakty v `.project-memory/hld/`.
*   **4.5 Finální schválení HLD**: Orchestrátor prezentuje HLD Business Vlastníkovi.

---

**Kapitola 5: Od HLD k implementaci: Low-Level Design, TDD a kódování**

*   **5.1 Plánování na základě HLD To-Do Listu**: Orchestrátor iniciuje sub-cykly.
*   **5.2 Detailní specifikace (LLD) – `spec-pseudocode` agent**: Výstup do `.project-memory/lld/feature_X/`.
*   **5.3 Příprava testů – `tdd` agent**: Testovací skripty (mimo `.project-memory/`, např. v `tests/`) a plány v `.project-memory/testing_artifacts/feature_X/`.
*   **5.4 Implementace – `code` agent**: Zdrojový kód (mimo `.project-memory/`, např. v `src/`) a poznámky v `.project-memory/code_implementation_notes/feature_X/`.
*   **5.5 Spuštění testů a Refinement Loop**.
*   **5.6 Bezpečnostní revize – `security-review` agent**.
*   **5.7 Finální dokumentace – `docs-writer` agent**: Na základě informací z `.project-memory/` a kódu generuje finální dokumentaci do adresáře `docs/`.
*   **5.8 Integrace – `integration` agent**.
*   **5.9 Revize s BV**.

---

**Kapitola 6: Zpětnovazební smyčky a lidský dohled**

*   **6.1 Automatizované zpětnovazební smyčky**.
*   **6.2 Role lidského dohledu**: BV, Technický Vedoucí, Scrum Master/Orchestrator Manager.
*   **6.3 Eskalační cesty**.
*   **6.4 Pravidelné "Synch Sessions"**: Zápisy v `.project-memory/idea_clarification/bv_architect_sync_log.md`.

---

**Kapitola 7: Škálovatelnost a správa kontextového okna**

*   **7.1 MCP (Model Context Protocol) Server / Summarizer Agent pro Orchestrátora**: Sumarizuje informace z `.project-memory/project_context/`.
*   **7.2 Využití `.project-memory/` jako distribuované paměti**.
*   **7.3 Vektorové databáze pro sémantické vyhledávání (pokročilá možnost)**.

---

**Kapitola 8: Měření úspěšnosti a kvality**

*   **8.1 Spokojenost zákazníka (BV)**.
*   **8.2 Kvalita kódu**: Vynucována postuláty, TDD, Security Review, lidskými revizemi.
*   **8.3 Efektivita procesu**.

---

**Kapitola 9: Pravidla a protokoly pro `SPARC Orchestrator`**

*   **9.1 Správa interní dokumentace (`.project-memory/`)**:
    *   **9.1.1 Vynucování struktury a syntaxe**: Zodpovědnost za standardy MD souborů, YAML frontmatter. Správa `.project-memory/project_meta/documentation_structure_config.md`.
    *   **9.1.2 Vytváření a aktualizace souborů**: Zapisuje výstupy agentů do `.project-memory/`.
    *   **9.1.3 Udržování To-Do listů**.
    *   **9.1.4 Správa Glosáře**: Aktualizace `.project-memory/project_meta/project_glossary.md`.
*   **9.2 Verzování pomocí Gitu (Model Context Protocol - Git Backend)**:
    *   **9.2.1 Zodpovědnost za commity**: Orchestrátor provádí commity změn v `.project-memory/` (a případně kódu).
    *   **9.2.2 Frekvence commitů**: Po každé smysluplné atomické změně.
    *   **9.2.3 Standard Semantic Commits**: Striktní dodržování.
    *   **9.2.4 Větvení (Branching Strategy)**: Počáteční práce na hlavní větvi.
    *   **9.2.5 Zpracování konfliktů**.
*   **9.3 Správa kontextu pro agenty**: Poskytuje odkazy na relevantní verze dokumentů.
*   **9.4 Komunikace a facilitace**: Hlavní komunikační bod mezi BV a AI agenty.

---

**Kapitola 10: Iterativní vývoj, správa změn a ad-hoc vstupy**

*   **10.1 Iterativní přidávání nových funkcionalit**: BV požadavek -> Orchestrátor záznam do `.project-memory/idea_clarification/` nebo dedikovaného souboru, analýza, prioritizace s BV -> Nový SPARC cyklus.
*   **10.2 Úprava existujících funkcionalit**: BV požadavek -> Orchestrátor záznam, analýza dopadu -> Modifikovaný SPARC cyklus.
*   **10.3 Zpracování upřesňujících údajů od BV (Ad-hoc vstupy)**:
    1.  BV poskytne vstup v chatu.
    2.  Orchestrátor zaznamená do `.project-memory/project_context/active_threads.md` nebo relevantního logu, vyhodnotí dopad.
    3.  Reakce na probíhající úkoly (přerušení a znovuzadání s aktualizací, nebo zahrnutí do dalšího kroku).
    4.  Transparentnost vůči BV.
*   **10.4 Role dílčích agentů při nejistotě**:
    *   Agenti nevolají jiné dílčí agenty přímo.
    *   Při problému ukončí úkol s `attempt_completion` (status: `clarification_needed` nebo `blocked_requires_X_decision`), dokumentují problém.
    *   Orchestrátor rozhodne o dalším postupu.
*   **10.5 Verzování a sledovatelnost změn**: Semantic commits v Gitu pro `.project-memory/`.

---

**Kapitola 11: Řešení konfliktů v AI-řízeném vývoji**

*   **11.1 Typy konfliktů**: Interpretace, priorit, technické, zdrojové, s postuláty.
*   **11.2 Systém detekce konfliktů**: Kontrola Orchestratorem, validační kroky agentů, hlášení od agentů.
*   **11.3 Formální proces řešení konfliktů**:
    *   Záznam do `.project-memory/project_context/conflict_resolution_log.md`.
    *   Klasifikace závažnosti (Level 1-3).
*   **11.4 Role "Mediator" Agenta (volitelný)**.
*   **11.5 Eskalační cesta a zapojení lidského dohledu**.
*   **11.6 Učení z konfliktů**: Analýza `conflict_resolution_log.md` pro zlepšení procesů.