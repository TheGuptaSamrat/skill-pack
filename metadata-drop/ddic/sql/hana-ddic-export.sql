SET SCHEMA "<ABAP_SCHEMA>";

SELECT
  l.TABNAME    AS "tabname",
  tt.DDTEXT    AS "ddtext",
  l.TABCLASS   AS "tabclass",
  l.CONTFLAG   AS "contflag",
  l.MAINFLAG   AS "mainflag",
  l.SQLTAB     AS "sqltab",
  l.CLIDEP     AS "clidep",
  ts.BUFALLOW  AS "bufallow",
  l.EXCLASS    AS "exclass",
  l.AS4LOCAL   AS "as4local",
  l.AS4VERS    AS "as4vers"
FROM DD02L l
LEFT JOIN DD02T tt
  ON tt.TABNAME = l.TABNAME
 AND tt.DDLANGUAGE = 'E'
LEFT JOIN DD09L ts
  ON ts.TABNAME = l.TABNAME
 AND ts.AS4LOCAL = l.AS4LOCAL
 AND ts.AS4VERS = l.AS4VERS
WHERE l.AS4LOCAL = 'A'
  AND (
    l.TABNAME LIKE '/BA1/%'
    OR l.TABNAME LIKE 'Z%'
    OR l.TABNAME LIKE 'Y%'
  )
ORDER BY l.TABNAME;

SELECT
  f.TABNAME     AS "tabname",
  f.FIELDNAME   AS "fieldname",
  f.POSITION    AS "position",
  f.KEYFLAG     AS "keyflag",
  f.ROLLNAME    AS "rollname",
  de.DOMNAME    AS "domname",
  de.DATATYPE   AS "datatype",
  de.LENG       AS "leng",
  de.DECIMALS   AS "decimals",
  ''            AS "notnull",
  ''            AS "checktable",
  f.REFTABLE    AS "reftable",
  f.REFFIELD    AS "reffield",
  dt.DDTEXT     AS "ddtext"
FROM DD03L f
LEFT JOIN DD04L de
  ON de.ROLLNAME = f.ROLLNAME
 AND de.AS4LOCAL = 'A'
LEFT JOIN DD04T dt
  ON dt.ROLLNAME = f.ROLLNAME
 AND dt.DDLANGUAGE = 'E'
WHERE f.AS4LOCAL = 'A'
  AND (
    f.TABNAME LIKE '/BA1/%'
    OR f.TABNAME LIKE 'Z%'
    OR f.TABNAME LIKE 'Y%'
  )
ORDER BY f.TABNAME, f.POSITION;

SELECT
  f.TABNAME    AS "tabname",
  f.FIELDNAME  AS "fieldname",
  'PRIMARY'    AS "keytype",
  f.POSITION   AS "position",
  ''           AS "checktable",
  ''           AS "checkfield",
  ''           AS "cardinality"
FROM DD03L f
WHERE f.AS4LOCAL = 'A'
  AND f.KEYFLAG = 'X'
  AND (
    f.TABNAME LIKE '/BA1/%'
    OR f.TABNAME LIKE 'Z%'
    OR f.TABNAME LIKE 'Y%'
  )
ORDER BY f.TABNAME, f.POSITION;
