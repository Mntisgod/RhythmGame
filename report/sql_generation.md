# 課題4

## 関数従属性や正規形についての考察
キーの指定をしようと関数従属性の和集合F+に変化はないので，極小被覆で考えよという意図で読む．

また，正規形については何を主キーに取ろうと変わらない．全てのスキーマはBCNFとなっている，
以下に課題3以前に設計した関係スキーマを再掲する．

<a id="schema"></a>
![スクリーンショット 2023-10-12 14 58 44](https://github.com/Mntisgod/isle4RhythmGame/assets/83445886/352541bf-7cd5-4a62-848b-2ca0b282fb90) 

各関係スキーマにおける関数従属性を以下に示す．

### players
主キーはplayer_idである．
得られる関数従属性は以下．
- player_id => player_name
- player_id => password
- player_id => mail_address

### playData
主キーは{player_id,chart_id}である．
得られる関数従属性は以下．
- {player_id, chart_id} => best_score
- {player_id, chart_id} => favorites

### chart
主キーはchart_idである．
関数従属性は以下．
- chart_id => chart_designer
- chart_id => song_id

### notes
主キーはnote_idである．
関数従属性は以下．
- note_id => note_type
- note_id => timing
- note_id => chart_id

### songs
主キーはsong_idである．
関数従属性は以下．
- song_id => difficulty
- song_id => title
- song_id => composer_name
- song_id => file_path

## 関係表の定義
上で示した関係スキーマに基づき，関係表をsql文で定義する．
各スキーマを定義するためのsql文は以下の通り．

```
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT NOT NULL,
    password TEXT NOT NULL,
    mail_address TEXT NOT NULL
);

CREATE TABLE playData (
    player_id INTEGER NOT NULL,
    chart_id INTEGER NOT NULL,
    best_score INTEGER DEFAULT NULL,
    favorites BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (player_id, chart_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (chart_id) REFERENCES charts(chart_id)
);

CREATE TABLE charts (
    chart_id INTEGER PRIMARY KEY,
    difficulty INTEGER NOT NULL,
    chart_designer TEXT,
    song_id INTEGER NOT NULL,
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
);

CREATE TABLE notes (
    note_id INTEGER PRIMARY KEY,
    note_type INTEGER NOT NULL,
    timing DOUBLE NOT NULL,
    chart_id INTEGER NOT NULL,
    lane INTEGER NOT NULL,
    FOREIGN KEY (chart_id) REFERENCES charts(chart_id)
);

CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    composer_name TEXT NOT NULL,
    file_path TEXT NOT NULL
);
```

## データの挿入
以下のように挿入を行った．

```
INSERT INTO players (player_id, player_name, password, mail_address) 
VALUES ('1', 'はるし', '2y$10$EmCWkpRPjtiparuEfUncR.eOwVAvCepMyJM/l.5pSDGyPu/eUJ48q', 'kuinfo334@gmail.com'),
       ('2', '港悪亜', '$2y$10$nKxr06Zqd4EQtPvl..NtkuGvIDGS44135jT.jEQ25SC8rMDoyGcMa', 'test@gmail.com');
...

INSERT INTO playData (player_id, chart_id, best_score, favorites) 
VALUES ('1', '1', '1000000', '0'),
       ('2', '1', '0', '1');
...

INSERT INTO charts (chart_id, difficulty, chart_designer, song_id)
VALUES ('1', '10', '譜面-2147483648号', '1'),
       ('2', '9', '譜面-2147483648号', '2'),
       ('3', '7', 'はるし', '1'),
       ('4', '0', 'はるし', '1');
...

INSERT INTO notes (note_id, note_type, timing, chart_id, lane)
VALUES ('1', '1', '0', '1', '0'),
('2', '1', '0.5', '1', '2'),
('3', '2', '1', '1', '3'),
('4', '1', '2', '1', '1'),
('5', '1', '2', '1', '2'),
('6', '1', '3', '1', '1');
....

INSERT INTO songs (song_id, title, composer_name, file_path)
VALUES ('1', 'ボリエール社畜', '苦茶の音楽工房', 'path/to/mp3'),
       ('2', '君が代', '林廣守', 'path/to/wav');
```

### 挿入後の出力

- players
```
1|はるし|2y$10$EmCWkpRPjtiparuEfUncR.eOwVAvCepMyJM/l.5pSDGyPu/eUJ48q|kuinfo334@gmail.com
2|港悪亜|$2y$10$nKxr06Zqd4EQtPvl..NtkuGvIDGS44135jT.jEQ25SC8rMDoyGcMa|test@gmail.com
```


- playData
```
1|1|1000000|0
2|1|0|1
```


- charts
```
1|10|譜面-2147483648号|1
2|9|譜面-2147483648号|2
3|7|はるし|1
4|0|はるし|1
```


- notes
```
1|1|0.0|1
2|1|0.5|1
3|2|1.0|1
4|1|2.0|1
5|1|2.0|1
6|1|3.0|1
```
- songs
```
1|ボリエール社畜|苦茶の音楽工房|path/to/mp3
2|君が代|林廣守|path/to/wav
```


