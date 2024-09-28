
# Language: pt

## PLUGIN RATING 

> **(1 - WER) * SIMILARITY * 100**

| PLUGIN | MODEL | RATING |
|--------|-------|--------|
| ovos-stt-plugin-fasterwhisper | small | 70.16188557553065 |
| ovos-stt-plugin-fasterwhisper | faster-whisper-small-pt-MyNorthAI | 59.430015245755584 |
| ovos-stt-plugin-chromium | chromium | 50.19274123169121 |
| ovos-stt-plugin-citrinet | stt_pt_citrinet_512_gamma_0_25 | 41.191327003259836 |
| ovos-stt-plugin-fasterwhisper | tiny | 37.82882992996792 |
| ovos-stt-plugin-fasterwhisper-zuazo | whisper-small-pt | 1.255941477049026 |
| ovos-stt-plugin-mms | mms-1b-all | 0 |

## Benchmarks


### DATASET: **All datasets**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.46875  | 0.7753661553554793 |
| ovos-stt-plugin-chromium         | chromium           | 0.35714285714285715  | 0.7807759747151966 |
| ovos-stt-plugin-mms         | mms-1b-all           | 1.01875  | 0.25798143639548865 |
| ovos-stt-plugin-fasterwhisper         | tiny           | 0.508209538702111  | 0.769206255650699 |
| ovos-stt-plugin-fasterwhisper         | small           | 0.24209575429087624  | 0.9257354866759527 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 0.30673316708229426  | 0.8572459033650356 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-pt           | 0.95  | 0.251188295409805 |


### DATASET: **cv_mls_psfb_zero_synthetic**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.7358301047496054  | 0.5941595264077886 |
| ovos-stt-plugin-chromium         | chromium           | 0.611453883879133  | 0.5654863624391026 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.6916343808293873  | 0.655427592849877 |
| ovos-stt-plugin-fasterwhisper         | tiny           | 0.7443037974683544  | 0.5589377559407372 |
| ovos-stt-plugin-fasterwhisper         | small           | 0.43071965628356607  | 0.7803649381101578 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 0.31467844869906725  | 0.8545296408141786 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-pt           | 0.42473812598651167  | 0.7833197252750865 |

### DATASET: **Speech-MASSIVE**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.2948396793587174  | 0.8960722141067261 |
| ovos-stt-plugin-chromium         | chromium           | 0.13131313131313133  | 0.9505462289778824 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.3807615230460922  | 0.8845362824804821 |
| ovos-stt-plugin-fasterwhisper         | tiny           | 0.508209538702111  | 0.769206255650699 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 0.21317635270541083  | 0.9346370138074561 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-pt           | 0.20220588235294118  | 0.9303357091850529 |

### DATASET: **common_voice_17_0**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.47368421052631576  | 0.8446499273750384 |
| ovos-stt-plugin-chromium         | chromium           | 0.5352697095435685  | 0.8020155582607275 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.5951417004048583  | 0.8120019249844465 |
| ovos-stt-plugin-fasterwhisper         | small           | 1.5512820512820513  | 0.18510972892231312 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 3.2714285714285714  | 0.18238985224765983 |

### DATASET: **fleurs**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.18359447004608295  | 0.924172486646157 |
| ovos-stt-plugin-chromium         | chromium           | 0.16962962962962963  | 0.9387642300379252 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.24589861751152073  | 0.9368372604089423 |
| ovos-stt-plugin-fasterwhisper         | small           | 0.14820276497695853  | 0.9568550415085466 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 0.1702127659574468  | 0.9357697951971784 |

### DATASET: **multilingual_librispeech**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.20087336244541484  | 0.9463737254181445 |
| ovos-stt-plugin-chromium         | chromium           | 0.2673425827107791  | 0.9018380181314256 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.20414847161572053  | 0.9528671069525496 |
| ovos-stt-plugin-fasterwhisper         | small           | 0.24209575429087624  | 0.9257354866759527 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 0.11408296943231441  | 0.9688357731116266 |

### DATASET: **common_voice_pt_pt**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 1.0232558139534884  | 0.1943452380952381 |
| ovos-stt-plugin-chromium         | chromium           | 1.0  | 0.15655827342757433 |
| ovos-stt-plugin-mms         | mms-1b-all           | 0.7833333333333333  | 0.4939189860341299 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-pt           | 0.85  | 0.48706660441954563 |

### DATASET: **MultiLingualSpeechRecognition_MLS-pt**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.3055555555555556  | 0.8954618616593365 |
| ovos-stt-plugin-chromium         | chromium           | 0.3155844155844156  | 0.868832504173699 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-pt           | 0.3263888888888889  | 0.9133885549220045 |

### DATASET: **mTEDx-ptbr**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.9932885906040269  | 0.0823601805619505 |
| ovos-stt-plugin-chromium         | chromium           | 1.0  | 0.09190755088941868 |
| ovos-stt-plugin-mms         | mms-1b-all           | 1.01875  | 0.25798143639548865 |
| ovos-stt-plugin-fasterwhisper-zuazo         | whisper-small-pt           | 0.95  | 0.251188295409805 |

### DATASET: **PTBRSpeechRecognition_CORAA**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|
| ovos-stt-plugin-citrinet         | stt_pt_citrinet_512_gamma_0_25           | 0.46875  | 0.7753661553554793 |
| ovos-stt-plugin-chromium         | chromium           | 0.35714285714285715  | 0.7807759747151966 |
| ovos-stt-plugin-fasterwhisper         | faster-whisper-small-pt-MyNorthAI           | 0.30673316708229426  | 0.8572459033650356 |
