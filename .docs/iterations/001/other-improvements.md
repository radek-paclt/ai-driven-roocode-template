# Návrh řešení ostatních identifikovaných problémů

## Úvod

Tento dokument popisuje návrh řešení pro ostatní problémy identifikované v základním end-to-end testu, kromě problému s příliš velkým kontextovým oknem orchestrátora, který je řešen v dokumentu `epic-coordinator-design.md`.

## 1. Agenti nevracejí výsledky zpět orchestrátorovi

### Problém
Auto-coder a Tester nevraceli výsledky zpět orchestrátorovi, což narušovalo workflow a vyžadovalo manuální zásah.

### Řešení

#### Úprava instrukcí pro Auto-Codera
- Zdůraznit nutnost vracení výsledků orchestrátorovi pomocí protokolu `attempt_completion`
- Přidat explicitní kontrolní seznam pro dokončení úkolu, který zahrnuje vrácení výsledků
- Přidat příklady správného použití protokolu `attempt_completion`

```json
{
  "taskId": "CODE-001",
  "result": "completed",
  "summary": "Implementace funkce pro přidání úkolu byla úspěšně dokončena",
  "outputArtifacts": [
    {
      "type": "code",
      "path": "src/tasks/add_task.py",
      "version": "1.0.0",
      "description": "Implementace funkce pro přidání úkolu"
    },
    {
      "type": "document",
      "path": ".project-memory/coding_guidelines_and_notes/add_task_implementation_notes.md",
      "version": "1.0.0",
      "description": "Poznámky k implementaci funkce pro přidání úkolu"
    }
  ],
  "metrics": {
    "testsPassing": 5,
    "codeLines": 120,
    "complexity": "low"
  },
  "nextSteps": [
    "Implementovat funkci pro úpravu úkolu",
    "Optimalizovat výkon funkce pro přidání úkolu"
  ]
}
```

#### Úprava instrukcí pro Testera
- Zdůraznit nutnost vracení výsledků testů orchestrátorovi pomocí protokolu `attempt_completion`
- Přidat explicitní kontrolní seznam pro dokončení úkolu, který zahrnuje vrácení výsledků
- Přidat příklady správného použití protokolu `attempt_completion` pro výsledky testů

```json
{
  "taskId": "TEST-001",
  "result": "completed",
  "summary": "Testy pro funkci přidání úkolu byly úspěšně vytvořeny a spuštěny",
  "outputArtifacts": [
    {
      "type": "code",
      "path": "tests/tasks/test_add_task.py",
      "version": "1.0.0",
      "description": "Testy pro funkci přidání úkolu"
    },
    {
      "type": "document",
      "path": ".project-memory/testing_strategy_and_plans/add_task_test_plan.md",
      "version": "1.0.0",
      "description": "Testovací plán pro funkci přidání úkolu"
    }
  ],
  "testResults": {
    "total": 5,
    "passing": 5,
    "failing": 0,
    "coverage": "95%"
  },
  "nextSteps": [
    "Vytvořit testy pro funkci úpravy úkolu",
    "Přidat testy pro hraniční případy"
  ]
}
```

## 2. Code si sám nekontroluje command line

### Problém
Auto-coder nekontroloval command line argumenty, což vedlo k chybám při spuštění aplikace.

### Řešení

#### Přidání standardního postupu pro kontrolu command line
- Vytvořit standardní šablonu pro kontrolu command line argumentů
- Přidat do instrukcí Auto-Codera povinnost implementovat kontrolu command line
- Přidat příklady správné implementace kontroly command line pro různé jazyky

##### Příklad pro Python:
```python
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Popis aplikace')
    parser.add_argument('--input', type=str, required=True, help='Vstupní soubor')
    parser.add_argument('--output', type=str, required=True, help='Výstupní soubor')
    parser.add_argument('--verbose', action='store_true', help='Podrobný výpis')
    
    # Kontrola argumentů
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    # Použití argumentů
    print(f"Vstupní soubor: {args.input}")
    print(f"Výstupní soubor: {args.output}")
    if args.verbose:
        print("Podrobný výpis je zapnutý")
    
    # Další kód aplikace
    
if __name__ == "__main__":
    main()
```

##### Příklad pro JavaScript (Node.js):
```javascript
const yargs = require('yargs');

// Definice a kontrola argumentů
const argv = yargs
  .option('input', {
    description: 'Vstupní soubor',
    type: 'string',
    demandOption: true
  })
  .option('output', {
    description: 'Výstupní soubor',
    type: 'string',
    demandOption: true
  })
  .option('verbose', {
    description: 'Podrobný výpis',
    type: 'boolean',
    default: false
  })
  .help()
  .alias('help', 'h')
  .argv;

// Použití argumentů
console.log(`Vstupní soubor: ${argv.input}`);
console.log(`Výstupní soubor: ${argv.output}`);
if (argv.verbose) {
  console.log('Podrobný výpis je zapnutý');
}

// Další kód aplikace
```

## 3. Sumarizace v průběhu mění kontextové okno

### Problém
Sumarizace v průběhu práce měnila kontextové okno, což narušovalo prompt caching.

### Řešení

#### Implementace inkrementální sumarizace
- Ukládat sumarizace do samostatných souborů v `.project-memory/project_context/summaries/`
- Implementovat inkrementální sumarizaci místo kompletní
- Vytvořit strukturu pro sumarizace, která umožňuje snadné načítání a aktualizace

```
.project-memory/
├── project_context/
│   ├── summaries/
│   │   ├── YYYY-MM-DD_HH-MM_summary.md
│   │   ├── YYYY-MM-DD_HH-MM_summary.md
│   │   └── ...
```

#### Formát sumarizačního souboru
```markdown
---
title: "Sumarizace projektu"
version: "1.0.0"
status: "Active"
created_by: "orchestrator"
created_date: "YYYY-MM-DDTHH:MM:SSZ"
summary_type: "incremental"
previous_summary: ".project-memory/project_context/summaries/YYYY-MM-DD_HH-MM_summary.md"
tags: ["summary", "project_state"]
---

# Sumarizace projektu k YYYY-MM-DD HH:MM

## Nové dokončené úkoly
- Úkol 1: Implementace funkce pro přidání úkolu
- Úkol 2: Vytvoření testů pro funkci přidání úkolu

## Aktuální stav projektu
- Dokončeno: 5 úkolů
- V průběhu: 3 úkoly
- Čeká: 7 úkolů

## Důležité rozhodnutí
- Rozhodnutí použít SQLite pro ukládání dat

## Další kroky
- Implementace funkce pro úpravu úkolu
- Vytvoření testů pro funkci úpravy úkolu
```

## 4. Správa gitu

### Problém
Chybí správný .gitignore a některé soubory nejsou přidány do gitu.

### Řešení

#### Vytvoření standardního .gitignore
- Vytvořit standardní .gitignore pro různé typy projektů
- Přidat specifické vzory pro RooCode

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# JavaScript
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.idea/
.vscode/
*.swp
*.swo
.DS_Store

# RooCode specifické
.roo/cache/
```

#### Úprava instrukcí pro správu gitu
- Přidat do role orchestrátora nebo EpicCoordinatora odpovědnost za správu gitu
- Zajistit používání `git add .` místo selektivního přidávání souborů
- Implementovat pravidelnou kontrolu nepřidaných souborů

```bash
# Přidání všech souborů do gitu
git add .

# Kontrola stavu
git status

# Commit s popisnou zprávou
git commit -m "feat(task): implementace funkce pro přidání úkolu"
```

## Závěr

Implementace těchto řešení pomůže vyřešit identifikované problémy a zlepšit celkovou kvalitu a efektivitu RooCode. Spolu s implementací role EpicCoordinator tvoří tyto změny první iteraci vylepšení RooCode.
