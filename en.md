
# Language: en

## PLUGIN RATING 

> **(1 - WER) * SIMILARITY * 100**

| PLUGIN | MODEL | RATING |
|--------|-------|--------|
| ovos-stt-plugin-mms | mms-1b-all | 79.81396764709378 |
| ovos-stt-plugin-citrinet | stt_en_citrinet_512_gamma_0_25 | 79.20138909935777 |
| ovos-stt-plugin-nemo | stt_en_quartznet15x5 | 78.67182904021747 |
| ovos-stt-plugin-fasterwhisper | large-v3 | 75.50050540329073 |
| ovos-stt-plugin-chromium | chromium | 74.22696935783833 |
| ovos-stt-plugin-fasterwhisper | tiny.en | 70.17058369052025 |
| ovos-stt-plugin-fasterwhisper | small.en | 0.1620044005362239 |

## Benchmarks


### DATASET: **All datasets**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.16884442629644753  | 0.9529069118365372 |
| ovos-stt-plugin-chromium         | chromium           | 0.2032436871278998  | 0.9316144492193519 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.16547749725576288  | 0.9564028217889171 |
| ovos-stt-plugin-fasterwhisper         | tiny.en           | 0.20761973008479637  | 0.8855670232428874 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.995508370763577  | 0.3606807062847417 |
| ovos-stt-plugin-fasterwhisper         | large-v3           | 0.17165541544601537  | 0.9114625339639706 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.17394855042874643  | 0.9523841291126673 |


### DATASET: **common_voice_17_0**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.24045940489193393  | 0.8823588042901114 |
| ovos-stt-plugin-chromium         | chromium           | 0.2733945569111141  | 0.858519757745789 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.26328462578751194  | 0.8964783703390297 |
| ovos-stt-plugin-fasterwhisper         | tiny.en           | 1.3655244029075804  | 0.1437241238417975 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 1.4444444444444444  | 0.19194814577520497 |
| ovos-stt-plugin-fasterwhisper         | large-v3           | 1.1900803871068446  | 0.23041116269767029 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.26816066536849403  | 0.891841159716081 |

### DATASET: **fleurs**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.157069157836029  | 0.9296278902066031 |
| ovos-stt-plugin-chromium         | chromium           | 0.12486017897091722  | 0.9362885985100915 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.12820037105751392  | 0.9501720049147251 |
| ovos-stt-plugin-fasterwhisper         | tiny.en           | 0.20280256553262688  | 0.9214219715217773 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.13252928053541552  | 0.9582789934523765 |
| ovos-stt-plugin-fasterwhisper         | large-v3           | 0.11259063022866704  | 0.9667789370927209 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.18418851087562743  | 0.9228826233622988 |

### DATASET: **gigaspeech**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.20039589706676264  | 0.9011337313686467 |
| ovos-stt-plugin-chromium         | chromium           | 0.25798930739237047  | 0.8143337632431776 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.24098886582374032  | 0.8590707445815854 |
| ovos-stt-plugin-fasterwhisper         | tiny.en           | 0.20761973008479637  | 0.8855670232428874 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.1759656652360515  | 0.9071677240123235 |
| ovos-stt-plugin-fasterwhisper         | large-v3           | 0.17165541544601537  | 0.9114625339639706 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.2187668282175552  | 0.8933574885579944 |

### DATASET: **peoples_speech**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.221532785510649  | 0.8372602596081192 |
| ovos-stt-plugin-chromium         | chromium           | 0.2124121378364478  | 0.8356563961468354 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.22277403334515786  | 0.8545653413075645 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.18719866999168744  | 0.8778219873426562 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.2137873754152824  | 0.8585894577097097 |

### DATASET: **voxpopuli**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.17820466352543193  | 0.9078611178204821 |
| ovos-stt-plugin-chromium         | chromium           | 0.24984493239052227  | 0.8171211841865486 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.09635811836115327  | 0.9614114755016411 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.1963271716805606  | 0.9080598268020966 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.2030328559393429  | 0.9074558255140556 |

### DATASET: **supreme-court-speech**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.26262626262626265  | 0.7474417287087537 |
| ovos-stt-plugin-chromium         | chromium           | 0.3217391304347826  | 0.6624433774059469 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.37337662337662336  | 0.6856730514433272 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.3540983606557377  | 0.6918824592613132 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.3344155844155844  | 0.6619973527668568 |

### DATASET: **Libriheavy-HQ**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_en_citrinet_512_gamma_0_25           | 0.16884442629644753  | 0.9529069118365372 |
| ovos-stt-plugin-chromium         | chromium           | 0.2032436871278998  | 0.9316144492193519 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.16547749725576288  | 0.9564028217889171 |
| ovos-stt-plugin-fasterwhisper         | small.en           | 0.995508370763577  | 0.3606807062847417 |
| ovos-stt-plugin-nemo         | stt_en_quartznet15x5           | 0.17394855042874643  | 0.9523841291126673 |
