
# Language: gl

## PLUGIN RATING 

> **(1 - WER) * SIMILARITY * 100**

| PLUGIN | MODEL | RATING |
|--------|-------|--------|
| ovos-stt-plugin-chromium | chromium | 69.01334403352972 |
| ovos-stt-plugin-nos | Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm | 61.148720990573125 |
| ovos-stt-plugin-fasterwhisper | small | 60.18192351385655 |
| ovos-stt-plugin-mms | mms-1b-all | 58.983969543763756 |
| ovos-stt-plugin-fasterwhisper-zuazo | whisper-small-gl | 0 |

## Benchmarks


### DATASET: **All datasets**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-chromium         | chromium           | 0.23732251521298176  | 0.9048824098013338 |
| ovos-stt-plugin-fasterwhisper         | small           | 0.3450258769407706  | 0.9188442931571251 |
| ovos-stt-plugin-nos         | Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm           | 0.3279112754158965  | 0.9098310796452163 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.3450413223140496  | 0.9005754340435855 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-gl           | 1.1053719008264462  | 0.29173900301555955 |


### DATASET: **common_voice_17_0**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-chromium         | chromium           | 0.21666666666666667  | 0.9405847797004896 |
| ovos-stt-plugin-fasterwhisper         | small           | 1.0615384615384615  | 0.16708406761969394 |
| ovos-stt-plugin-nos         | Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm           | 0.25  | 0.9210770310212347 |

### DATASET: **fleurs**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-chromium         | chromium           | 0.2357503385448726  | 0.9233926530375933 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.2540973505853358  | 0.9436295417486564 |
| ovos-stt-plugin-fasterwhisper         | small           | 0.3450258769407706  | 0.9188442931571251 |
| ovos-stt-plugin-nos         | Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm           | 0.3279112754158965  | 0.9098310796452163 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-gl           | 0.18188539741219964  | 0.9452973414937542 |

### DATASET: **openslr**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-chromium         | chromium           | 0.23732251521298176  | 0.9048824098013338 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.3450413223140496  | 0.9005754340435855 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-gl           | 1.1053719008264462  | 0.29173900301555955 |
