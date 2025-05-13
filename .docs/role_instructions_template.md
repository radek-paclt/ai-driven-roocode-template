# Šablona instrukcí pro role v rooCode Boomerang Mode

Tato šablona definuje jednotnou strukturu pro instrukce všech rolí v rooCode Boomerang Mode. Každá role bude mít svůj vlastní soubor s instrukcemi, který bude následovat tuto strukturu, ale bude obsahovat specifické informace relevantní pro danou roli.

## Struktura instrukcí

```markdown
# [Název role]

## Úvod
Stručný popis role, její hlavní odpovědnosti a místo v celkovém workflow. Tato sekce by měla jasně definovat, kdo agent je a jaký je jeho hlavní účel.

## Klíčové odpovědnosti
Detailní seznam hlavních odpovědností role:

1. **[Odpovědnost 1]**
   - Podrobný popis první odpovědnosti
   - Konkrétní úkoly a očekávané výstupy
   - Kritéria úspěchu

2. **[Odpovědnost 2]**
   - Podrobný popis druhé odpovědnosti
   - Konkrétní úkoly a očekávané výstupy
   - Kritéria úspěchu

3. **[Odpovědnost 3]**
   - ...

## Workflow a procesy
Detailní popis pracovních postupů a procesů, které role následuje:

### [Proces 1]
1. Krok 1
2. Krok 2
3. Krok 3
   - Podrobnosti
   - Příklady

### [Proces 2]
1. Krok 1
2. Krok 2
3. Krok 3
   - Podrobnosti
   - Příklady

## Komunikační protokoly
Popis komunikačních protokolů, které role používá:

### Příjem úkolů
Jak role přijímá úkoly od Orchestratora:
- Formát zprávy `new_task`
- Zpracování kontextu a vstupů
- Potvrzení přijetí úkolu

### Hlášení o dokončení
Jak role hlásí dokončení úkolů Orchestratorovi:
- Formát zprávy `attempt_completion`
- Obsah a struktura výstupů
- Hlášení problémů a žádosti o upřesnění

### Spolupráce s ostatními rolemi
Jak role spolupracuje s ostatními agenty:
- S kterými rolemi nejčastěji spolupracuje
- Jaké informace si vyměňují
- Jak řeší konflikty a nejasnosti

## Práce s .project-memory
Detailní instrukce pro práci s adresářem `.project-memory`:

### Čtení dokumentů
- Které adresáře a soubory role čte
- Jak interpretuje metadata a strukturu dokumentů
- Jak pracuje s verzemi dokumentů

### Vytváření a úprava dokumentů
- Které adresáře a soubory role vytváří nebo upravuje
- Formát a struktura vytvářených dokumentů
- Pravidla pro metadata a verzování

## Omezení a hranice
Jasná definice toho, co role NEMÁ dělat:

- Neměla by zasahovat do odpovědností jiných rolí
- Neměla by překračovat své oprávnění
- Neměla by provádět vlastní invenci mimo zadané úkoly
- Specifická omezení pro danou roli

## Use Cases
Konkrétní příklady typických scénářů, ve kterých role působí:

### Use Case 1: [Název]
**Kontext:** Popis situace a kontextu
**Úkol:** Co má role udělat
**Postup:**
1. Krok 1
2. Krok 2
3. Krok 3
**Výstup:** Očekávaný výsledek
**Poznámky:** Důležité informace a tipy

### Use Case 2: [Název]
**Kontext:** Popis situace a kontextu
**Úkol:** Co má role udělat
**Postup:**
1. Krok 1
2. Krok 2
3. Krok 3
**Výstup:** Očekávaný výsledek
**Poznámky:** Důležité informace a tipy

## Kritéria kvality
Specifická kritéria pro hodnocení kvality práce role:

1. **[Kritérium 1]**
   - Jak měřit a hodnotit
   - Příklady dobré a špatné praxe

2. **[Kritérium 2]**
   - Jak měřit a hodnotit
   - Příklady dobré a špatné praxe

3. **[Kritérium 3]**
   - ...

## Řešení problémů
Návod, jak postupovat při běžných problémech:

### Problém 1: [Popis]
**Příznaky:** Jak problém rozpoznat
**Řešení:** Kroky k vyřešení problému
**Prevence:** Jak problému předcházet

### Problém 2: [Popis]
**Příznaky:** Jak problém rozpoznat
**Řešení:** Kroky k vyřešení problému
**Prevence:** Jak problému předcházet
```

## Pokyny pro vytváření instrukcí

1. **Délka a detailnost**
   - Instrukce by měly být dostatečně detailní, ale nepřekročit 300-400 řádků
   - Zaměřte se na konkrétní postupy a příklady, ne obecné fráze
   - Používejte odrážky a číslované seznamy pro přehlednost

2. **Jazyk a styl**
   - Používejte jasný, přímý jazyk
   - Vyhněte se dvojznačnostem a nejasnostem
   - Používejte aktivní slovesa a konkrétní příklady

3. **Příklady a use cases**
   - Zahrňte konkrétní příklady pro každou hlavní odpovědnost
   - Use cases by měly pokrývat typické i méně obvyklé scénáře
   - Příklady by měly být realistické a relevantní pro danou roli

4. **Integrace s .project-memory**
   - Jasně definujte, které části `.project-memory` role používá
   - Specifikujte formát a strukturu dokumentů, které role vytváří
   - Vysvětlete, jak role pracuje s verzemi dokumentů

5. **Omezení a hranice**
   - Jasně definujte, co role NEMÁ dělat
   - Specifikujte, kdy by měla role eskalovat problém Orchestratorovi
   - Vysvětlete, jak se vyhnout překrývání odpovědností s jinými rolemi
