# Testovací scénář: Test bezpečnostní revize

## Cíl testu
Otestovat schopnost systému identifikovat a řešit bezpečnostní problémy. Tento test ověří, zda security-review agent dokáže efektivně analyzovat kód, identifikovat potenciální bezpečnostní rizika a navrhnout jejich řešení.

## Počáteční instrukce pro orchestrátora
```
Vytvoř jednoduchou webovou aplikaci pro správu uživatelských účtů s následujícími funkcemi:
1. Registrace nových uživatelů
2. Přihlášení existujících uživatelů
3. Změna hesla
4. Resetování zapomenutého hesla
5. Zobrazení a úprava uživatelského profilu
6. Administrátorský přístup pro správu uživatelů

Aplikace by měla být implementována v Node.js s využitím Express frameworku a ukládat data v MongoDB. Implementuj aplikaci s důrazem na funkčnost, ale záměrně zanech několik běžných bezpečnostních problémů, jako jsou:
- Ukládání hesel v nešifrované podobě
- Zranitelnost vůči SQL/NoSQL injection
- Nedostatečná validace vstupů
- Chybějící CSRF ochrana
- Nedostatečné ošetření session

Vytvoř kompletní řešení včetně specifikace, architektury, implementace, testů a dokumentace. Po dokončení implementace proveď bezpečnostní revizi a oprav nalezené problémy.
```

## Očekávané výstupy

### Soubory
- `.project-memory/project_meta/project_overview.md`: Přehled projektu s popisem aplikace
- `.project-memory/lld/user_management/`: Adresář obsahující low-level design aplikace
- `.project-memory/testing_strategy_and_plans/`: Adresář obsahující testovací plány
- `.project-memory/security_review/`: Adresář obsahující bezpečnostní analýzu a doporučení
- `src/`: Adresář obsahující implementaci aplikace
- `tests/`: Adresář obsahující testy
- `README.md`: Dokumentace projektu
- `package.json`: Definice závislostí projektu

### Struktura projektu
```
.
├── .project-memory/
│   ├── project_meta/
│   │   ├── project_overview.md
│   │   └── ...
│   ├── lld/
│   │   ├── user_management/
│   │   │   ├── user_management_spec.md
│   │   │   └── ...
│   │   └── ...
│   ├── testing_strategy_and_plans/
│   │   ├── user_management_test_plan.md
│   │   └── ...
│   ├── security_review/
│   │   ├── security_analysis.md
│   │   ├── vulnerability_report.md
│   │   ├── remediation_plan.md
│   │   └── ...
│   └── ...
├── src/
│   ├── server.js
│   ├── routes/
│   │   ├── auth.js
│   │   ├── users.js
│   │   └── ...
│   ├── controllers/
│   │   ├── authController.js
│   │   ├── userController.js
│   │   └── ...
│   ├── models/
│   │   ├── user.js
│   │   └── ...
│   ├── middleware/
│   │   ├── auth.js
│   │   └── ...
│   └── ...
├── tests/
│   ├── auth.test.js
│   ├── users.test.js
│   └── ...
├── README.md
└── package.json
```

## Kritéria úspěchu
- Aplikace byla nejprve implementována s bezpečnostními nedostatky
- Security-review agent identifikoval bezpečnostní problémy
- V `.project-memory/security_review/` je zdokumentována bezpečnostní analýza a nalezené zranitelnosti
- Bezpečnostní problémy byly opraveny
- Opravená aplikace je funkční a splňuje všechny požadavky
- Kód je dobře strukturovaný a následuje best practices
- Testy pokrývají všechny základní funkce a hraniční případy
- Dokumentace je kompletní a srozumitelná
- Bezpečnostní revize pokrývá všechny běžné typy zranitelností (OWASP Top 10)

## Časový limit
120 minut

## Postup testování
1. Vytvoření git větve: `git checkout -b test/security-review`
2. Předání počáteční instrukce orchestrátorovi
3. Čekání na dokončení úkolu (max. 120 minut)
4. Kontrola vytvořených souborů a jejich obsahu
5. Analýza bezpečnostní revize a provedených oprav
6. Ověření funkčnosti aplikace
7. Vyhodnocení testu podle kritérií úspěchu

## Poznámky k vyhodnocení
- Klíčovým aspektem tohoto testu je schopnost security-review agenta identifikovat a řešit bezpečnostní problémy
- Je třeba sledovat, jak security-review agent komunikuje s ostatními agenty při řešení bezpečnostních problémů
- Důležité je, aby bezpečnostní analýza byla důkladná a pokrývala všechny běžné typy zranitelností
- Opravy bezpečnostních problémů by měly být efektivní a neměly by narušit funkčnost aplikace
