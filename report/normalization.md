# 課題3

京都大学工学部情報学科 3回　計算機　1029332978 上野山遼音

## 得られた各関係スキーマの関数従属性
以下に得られた関係スキーマを再掲する．

<a id="schema"></a>
![スクリーンショット 2023-10-12 14 58 44](https://github.com/Mntisgod/isle4RhythmGame/assets/83445886/352541bf-7cd5-4a62-848b-2ca0b282fb90) 

また，各関係スキーマにおける関数従属性を以下に示す．

### players
- player_id => player_name
- player_id => password
- player_id => mail_address
- player_name => player_id
- player_name => password
- player_name => mail_address
- mail_address => player_id
- mail_address => password
- mail_address => player_name

### playData
- {player_id, chart_id} => best_score
- {player_id, chart_id} => favorites

### chart
- chart_id => chart_designer
- chart_id => song_id

### notes
- note_id => note_type
- note_id => timing
- note_id => chart_id

### songs

- song_id => difficulty
- song_id => title
- song_id => composer_name
- song_id => file_path
- {title, composer_name} => song_id
- {title, composer_name} => difficulty
- {title, composer_name} => file_path
- file_path => difficulty
- file_path => title
- file_path => song_id
- file_path => composer_name

## 関係スキーマの再設計

上述した自明でない関数従属性は，全てBCNFの条件: **関数従属性 Y->Aが成立するならば，Yは超キーである．**

を満たしているので，BCNFである．よって，これ以上の正規化は情報の損失を伴う可能性があるため，再設計の必要はないと考える．


## 考察
もし再設計が必要となるようなER図を作るのであれば，以下の図のようなものを考えれば良いだろう，
![スクリーンショット 2023-10-13 9 46 26](https://github.com/Mntisgod/isle4RhythmGame/assets/83445886/d44171ea-23b6-48f3-9489-d3b8810e7e4f)

この図では，元はnotesテーブルにあったものをnote型のリストとしてデータを格納することにしている．
note型は，{note_id, note_type, timing, chart_id}といったデータを格納した型である．
もしこのようなスキーマを設計した場合，その部分は1NFですらなくなる．なぜなら，**notes_list属性の取りうる値が単純値でなく，値の集合となっている**からである．

この場合は，元通りnotesテーブルを設計することで単純値を属性の取りうる値とし，1NFをクリアさせ，元通りBCNFの条件を満たさせることができる．


