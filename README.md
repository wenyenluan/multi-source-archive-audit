# Multi-source Archive Audit

[English](#english) · [繁體中文](#繁體中文)

A reusable Codex skill for comparing archive inventories across local disks, cloud drives, websites, databases, and media platforms without turning uncertainty into false missing-file claims.

---

## English

### What this skill does

Use this skill when the same collection exists in several places and you need to know what is truly matched, missing, extra, incomplete, conflicting, or still uncertain.

It helps Codex:

- define the baseline and the role of every source;
- record pagination, API caps, inaccessible folders, and scan timestamps;
- preserve raw names and provenance while deriving canonical IDs and variants;
- compare exact IDs, variants, hashes, and supporting metadata in evidence order;
- keep `matched`, `baseline_only`, `comparison_only`, `variant_incomplete`, `conflict`, and `uncertain` results separate;
- produce a gap report with explicit coverage and safe next actions.

The audit is read-only by default. It does not authorize deleting, renaming, downloading, uploading, merging, or publishing content.

### Install

The easiest option is to give Codex this repository URL and ask:

> Install the `multi-source-archive-audit` skill from https://github.com/wenyenluan/multi-source-archive-audit

Alternatively, place this repository folder in your Codex skills directory so that `SKILL.md` is located at:

```text
<your-skills-directory>/multi-source-archive-audit/SKILL.md
```

Restart or refresh Codex if the skill does not appear immediately.

### Use

Invoke it explicitly with `$multi-source-archive-audit`, or ask Codex to compare archive inventories and produce an evidence-backed gap report.

Example prompt:

```text
Use $multi-source-archive-audit to compare these two CSV inventories.

Baseline: cloud-export.csv
Comparison: local-disk.csv
Identity rule: canonical_id + variant

The cloud export returned exactly 1,000 rows and the API has a 1,000-row cap.
Produce a gap report, keep uncertain records separate, and do not modify any files.
```

Useful inputs include:

- one inventory per source in CSV, JSON, database export, or structured table form;
- the baseline and completeness standard;
- known API, pagination, authentication, or folder-depth limits;
- stable source IDs, canonical IDs, variants, hashes, sizes, dates, and durations;
- the scan time and any excluded locations.

### Optional deterministic CSV comparison

The bundled helper performs a conservative exact comparison using `canonical_id` and `variant`:

```text
python3 scripts/compare_inventories.py baseline.csv comparison.csv \
  --output audit-results.csv
```

Required column:

- `canonical_id`

Optional column:

- `variant`

The helper intentionally does not perform fuzzy title matching. Rows without a canonical ID are classified as `uncertain` for manual review.

### Expected report

A good result contains:

1. audit question and source roles;
2. collection time and coverage limits;
3. normalization and matching rules;
4. totals with denominators;
5. results by taxonomy;
6. conflicts and uncertain records;
7. validation sample;
8. safe next actions.

If a source is capped or incomplete, the report must say “not observed in the scanned inventory” instead of claiming that an item is definitively missing.

---

## 繁體中文

### 這個 skill 能做什麼

當同一批典藏內容分散在本機硬碟、雲端硬碟、網站、資料庫或影音平台時，可以使用這個 skill 判斷哪些項目確實相符、缺少、多出、版本不完整、互相衝突，或仍缺乏足夠證據。

它會協助 Codex：

- 定義基準來源與每個來源的角色；
- 記錄分頁、API 筆數上限、無法存取的資料夾與掃描時間；
- 保留原始檔名與來源，同時解析 canonical ID 與版本；
- 依證據強度比較精確 ID、版本、雜湊與輔助 metadata；
- 分開呈現「相符、僅基準來源有、僅比較來源有、版本不完整、衝突、不確定」；
- 產生交代涵蓋率、限制與安全下一步的差異報告。

典藏稽核預設為唯讀。它不代表你已授權刪除、改名、下載、上傳、合併或公開任何內容。

### 安裝

最簡單的方式是把這個 repository 網址交給 Codex，並告訴它：

> 請從 https://github.com/wenyenluan/multi-source-archive-audit 安裝 `multi-source-archive-audit` skill。

也可以把整個 repository 資料夾放進 Codex 的 skills 目錄，並確認檔案位於：

```text
<你的-skills-目錄>/multi-source-archive-audit/SKILL.md
```

如果沒有立即出現，請重新啟動或重新整理 Codex。

### 使用方式

可以明確輸入 `$multi-source-archive-audit`，或直接請 Codex 比較多份典藏清單並產生有證據的差異報告。

範例提示詞：

```text
請使用 $multi-source-archive-audit 比較這兩份 CSV 清單。

基準來源：cloud-export.csv
比較來源：local-disk.csv
識別規則：canonical_id + variant

雲端匯出剛好回傳 1,000 筆，而 API 上限也是 1,000 筆。
請產生差異報告，把不確定項目分開，並且不要修改任何檔案。
```

建議提供：

- 每個來源各自的 CSV、JSON、資料庫匯出或結構化表格；
- 哪一個來源是基準，以及你所認定的完整標準；
- API、分頁、登入權限與資料夾深度限制；
- 來源 ID、canonical ID、版本、雜湊、容量、日期與影音長度；
- 掃描時間與未納入的位置。

### 選用的精確 CSV 比對工具

內附工具會使用 `canonical_id` 與 `variant` 做保守的精確比對：

```text
python3 scripts/compare_inventories.py baseline.csv comparison.csv \
  --output audit-results.csv
```

必要欄位：

- `canonical_id`

選用欄位：

- `variant`

工具刻意不做模糊標題配對。沒有 canonical ID 的資料會標為 `uncertain`，留待人工確認。

### 預期報告內容

一份完整結果應包含：

1. 稽核問題與來源角色；
2. 蒐集時間與涵蓋限制；
3. 正規化與配對規則；
4. 附分母的統計；
5. 依結果分類呈現差異；
6. 衝突與不確定項目；
7. 抽樣驗證；
8. 安全的下一步。

如果來源有筆數上限或盤點不完整，報告應寫「未在本次掃描清單中觀察到」，而不是直接宣稱檔案確實遺失。

## License

MIT
