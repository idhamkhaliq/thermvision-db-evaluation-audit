# Paper 1 Handoff Checkpoint v2.0 - MVA WRITING / EXPERIMENTS CLOSED

**Tanggal checkpoint:** 22 September 2026 (Asia/Jakarta)  
**Project:** Paper #3; fokus dokumen: Paper 1  
**Versi kontrak ilmiah:** v1.0, tidak berubah  
**Versi handoff:** v2.0, bukan kontrak eksperimen v2.0

> **Baca ini lebih dahulu: eksperimen Paper 1 DITUTUP. Target kerja adalah Machine Vision and Applications (MVA), melalui jalur subscription/non-OA dengan anggaran APC 0. Tugas berikutnya adalah menulis Manuscript Draft v1 dari bukti yang sudah ada. Jangan menjalankan ulang ekstraksi, merancang eksperimen baru, atau mengulang pemilihan jurnal.**

Dokumen ini adalah checkpoint operasional dan indeks bukti. Ia tidak menggantikan kontrak ilmiah, file hasil asli, atau keputusan penulis manusia. Versi terbaru memperbarui status pekerjaan dan arah penulisan; tidak mengubah metode atau angka. Semua outcome ArcFace dan AdaFace telah terlihat. Label outcome-blind dalam log lama hanya berlaku pada tahap yang dicatat, bukan status penelitian sekarang.

## Cara menggunakan paket ini

1. Baca bagian 0-2 untuk status dan hierarki otoritas.
2. Baca bagian 3-9 untuk desain, angka, hasil, dan batas penafsirannya.
3. Ikuti bagian 12-17 untuk penulisan MVA, pekerjaan tersisa, dan larangan perubahan.
4. Gunakan resume command bagian 20 ketika berpindah chat/researcher.
5. Manifest paket dapat dicek dengan `python verify_handoff.py .`; skrip itu hanya membaca dan memeriksa file, bukan menjalankan eksperimen.

**Kode sumber:** [S0] handoff ilmiah v1.0; [S1] hasil ArcFace; [S2] hasil B2-G; [S3] hasil AdaFace; [S4] Final Evidence Synthesis; [D] keputusan eksplisit pengguna dalam percakapan; [G1-G5] pedoman penulisan/publikasi. Locator dan hash berada pada bagian 21 serta registry JSON.

## 0. Status operasional saat handoff

| Komponen | Status |
| --- | --- |
| Experiment execution | CLOSED - disepakati pengguna |
| Methodology | v1.0 LOCKED |
| Literature/claim gate | LOCKED; verifikasi sitasi yang dipakai masih bagian penulisan |
| Dataset gate | GREEN |
| ArcFace extraction + fresh-runtime integrity | COMPLETE + PASS (execution record) |
| Confirmatory A/B/C/D | COMPLETE |
| A2, B2-G, C2, C3 | COMPLETE |
| AdaFace checkpoint + E | LOCKED + COMPLETE |
| Final Evidence Synthesis | v1 COMPLETE |
| Target jurnal | MVA - dipilih pengguna; belum disubmit |
| Anggaran biaya wajib | 0; tidak bergantung pada waiver |
| Manuscript Draft v1 | BELUM DIBUAT dalam record yang tersedia |
| Fase aktif | MANUSCRIPT PREPARATION |
| Eksperimen baru yang diotorisasi | Tidak ada |

**NEXT ACTION:** susun kerangka argumentasi dan pemetaan sumber/tabel untuk MVA, lalu mulai Draft v1. Penulisan dapat dimulai dengan placeholder yang jelas untuk metadata penulis yang belum tersedia; jangan menunggu semua urusan administratif selesai untuk menulis isi.

Penutupan eksperimen bukan jaminan paper diterima, bukan sertifikasi Q1, dan bukan alasan menyembunyikan kesalahan validitas. Koreksi yang benar-benar diperlukan mengikuti change control pada bagian 18. [D; S4 bagian 12-13]

## 1. Hierarki otoritas - pisahkan metode, hasil, status, dan format

| Ranah | Otoritas utama | Aturan konflik |
| --- | --- | --- |
| Metodologi ilmiah | Experiment Contract v1.0 lalu Config v1.0 | Mengalahkan draft/saran lama. Handoff v2.0 tidak menulis ulang kontrak. |
| Corpus/preprocessing | Final hash audit, canonical manifest, bbox patch, QC, checkpoint/crop locks | Jangan mengganti file final dengan reviewed/PENDING. |
| Pelaksanaan aktual | Completion records, adapter/frame-plan/mapping dan hasil asli S1-S3 | Menunjukkan apa yang diekspor. Ketidakcocokan dengan kontrak harus dicatat, bukan diselaraskan diam-diam. |
| Angka Results | CSV hasil asli di S1-S3 | S4 dan dokumen ini adalah sintesis/indeks, bukan pengganti data. |
| Interpretasi evidence | S4 + batas klaim kontrak | Revisi bahasa boleh; hasil/estimand tidak boleh diganti untuk memperkuat cerita. |
| Status dan pekerjaan berikutnya | Keputusan terbaru pengguna [D] + handoff v2.0 | Menggantikan instruksi lama untuk mulai ekstraksi/AdaFace atau kembali memilih jurnal. |
| Format submission | Pedoman resmi MVA saat submission | Mengatur format/deklarasi, tidak mengotorisasi perubahan eksperimen. |

**Jangan mencampur versi:** contract v1.0; adapter/technical patch v1.1; B2-G recovery v2; evidence synthesis v1; handoff v2.0 adalah objek berbeda. Nomor versi technical patch bukan bukti perubahan hipotesis. [S0-S4]

## 2. Baseline file registry dan status verifikasi

### 2.1 Baseline ilmiah sebelum outcome

Hash berikut dipertahankan dari [S0, bagian 1.1]. **File asli di tabel ini tidak tersedia sebagai raw bytes dalam set lampiran yang diperiksa pada handoff ini; hash tidak dihitung ulang.** Ini tidak membuktikan file hilang dari Drive. Jangan menciptakan ulang byte file lalu mengaku identik dengan hash tersebut.

| File baseline | Peran pada record S0 | SHA256 expected |
| --- | --- | --- |
| `Paper1_Experiment_Contract_v1_0_LOCKED.md` | Scientific source of truth | `c4ff591146d28d484af151eaae021c60f6cd44d04b5d1a94c583dc892b0d3eb1` |
| `Paper1_Experiment_Config_v1_0_LOCKED.json` | Machine-readable frozen config | `37eca5822b2f05ace396b45c35f0f8e759943caac6cd56106533694393558090` |
| `Paper1_Final_Hash_Audit_v1_0.md` | Human-readable promotion audit | `65b7bde7e1f101717947f8280b20574a93e7e0a3b37880115ffa467b916b1420` |
| `Paper1_Final_Hash_Audit_v1_0.json` | Machine-readable promotion audit | `ef208b227e0cef8b88997f91e8d0bbea3126d549bd869f04e5844ac7e1c0fd4e` |
| `canonical_manifest_v1_final.csv` | Authoritative 100-video corpus | `04dfceccff2adff2ed3a40ea9cd1096d57e03c11e8f05bdbbd69121c81bd9eaf` |
| `bbox_patch_v1_final.csv` | Authoritative bbox corrections | `b63a2b480bf18059ed83741150b7ce560c1d07f9acb84623d0e23b42e65ebafe` |
| `visual_qc_decisions_final.csv` | Final visual-QC decisions | `fe043ad0b2405a1323f5d6464065ce31d3b28eb5400d4a046e59d44982aa4f4d` |
| `Paper1_ArcFace_Checkpoint_Lock_v1.json` | Primary encoder lock | `1716dad7b34b6b386a3a47ffb6a33e114dbd308cd4b2a575f72901689dcec0ab` |
| `Paper1_FaceCrop_Expansion_Lock_v1.json` | Crop factor lock | `340602df9e87b6af5696aadfac2b4ffed602e2dbfadf225195592d969053b7c3` |
| `Final_Claim_Literature_Matrix_Paper1.md` | Novelty/claim literature lock | `e96f990ea67c28258164b2dad85fac626a99f74a68bc869acd8bade5b5ae022e` |
| `Paper1_Main_Frozen_Embedding_Extraction_v1.ipynb` | Next execution notebook | `d2d9e1491349fc71678a76bde28bf2ce43eba526c750a927e4ea54d01e14ff9e` |
| `Paper1_Main_Frozen_Embedding_Extraction_v1_README.md` | Extraction run instructions | `526baef5c03a01e733b6653263f5df19de59c08918bd9fb390c5bdf2ad5b6656` |

Sumber tabel di atas sendiri tersedia dan diverifikasi: `Paper1_Handoff_Checkpoint_v1_0_LOCKED.md`, SHA256 `7693c38f874962e4b3e9f695f86b769857720527b6588dfd294c5c3fda625860`. Salinan ini tetap arsip historis untuk metode; status NOT YET RUN/NOT YET FROZEN di dalamnya sudah superseded.

### 2.2 Paket hasil dan sintesis - bytes diverifikasi pada handoff ini

| ID | File | Bytes | SHA256 |
| --- | --- | --- | --- |
| S1 | `Paper1_Confirmatory_Results_v1.zip` | 246751 | `66b793dfff4b7aa68a7a523b7831d6108f79217d574d5a79f7c611ac186c47f6` |
| S2 | `Paper1_B2G_Defensive_Results_v2.zip` | 339820 | `e64aa90e7b4623a4de107e6125f7e06bad84f91b87a07360964863e64ed31004` |
| S3 | `Paper1_Robustness_E_AdaFace_Results_v1_1.zip` | 30108 | `a8793adfbe40ace1f1b746a8a5a081b691583a026d803d17996e1d084bee1237` |
| S4 | `Paper1_Final_Evidence_Synthesis_v1.zip` | 1496961 | `62ad1ef58f776ff00bd3b740c7ef4adba4ea1e0d2699e25c3e7cf5e4a6c5d585` |

Manifest internal terverifikasi: **S1 15/15; S2 3/3; S3 12/12**, yaitu 30 entry sumber. **S4 31/31** entry sintesis juga cocok. Ketiga ZIP sumber yang tersimpan di S4 identik byte-for-byte dengan ZIP standalone yang dilampirkan. Angka ini adalah jumlah entry manifest, bukan jumlah eksperimen atau subjek.

Handoff ini tidak membuka Drive live, memproses raw video, memuat weights, menjalankan bootstrap baru, atau mengaudit kembali validitas setiap perhitungan dari inference. Pemeriksaan yang dilakukan adalah integritas bytes/manifest, pembacaan completion records, dan pemindahan nilai yang sudah diekspor.

### 2.3 Berkas utama di dalam Final Evidence Synthesis

| File | SHA256 |
| --- | --- |
| `Paper1_Final_Evidence_Synthesis_v1.md` | `27e1bd906656fa8cd5798314057b7663d0b2c198be7fe59f61712c146c6b57ce` |
| `Paper1_Final_Evidence_Synthesis_v1.docx` | `47964ea8121f2f30af59322a4f32e345693f9aacd380d18eef2bd239a240cd0d` |
| `Paper1_Manuscript_Tables_v1.xlsx` | `3b1c1de6af554c13f99f818e7e88f3e335292866aa4b78ecbb9efecfaf5c14e3` |

S4 juga menyimpan sembilan CSV tabel, empat figure PNG/SVG, captions, Reporting_Decisions, Source_Index, dan quality-check records. Berkas DOCX/XLSX adalah artefak sintesis yang sudah ada, bukan Draft v1 MVA. Bundle handoff mempertahankan S4 tanpa memodifikasi isi.

### 2.4 Literatur dan riwayat yang tersedia

`Scopus_P1_Review.md` dan `Scopus_P1_Literature_Matrix.csv` adalah mapping awal; bukan kontrak ilmiah final. Keduanya masih dapat memuat judul/saran lama seperti identity-disjoint split atau full factorial yang tidak dilakukan. `Continue Paper Execution.txt` merupakan riwayat, bukan sumber numerical ground truth. File `Thermal Face Paper Watch.txt` mempunyai banyak versi/judul sama; jangan memilih hanya berdasarkan basename.

Final Claim-Literature Matrix tercatat LOCKED pada [S0], tetapi raw file finalnya tidak disertakan ulang di set handoff ini. Gunakan locator/hash untuk mencarinya ketika memerlukan detail. Jangan menyatakan seluruh 14 full text tersedia/selesai diaudit berdasarkan mapping awal saja. Penulis harus memverifikasi referensi yang benar-benar masuk manuskrip. [S0; catatan literature gate]

## 3. Scientific locks: kontribusi, populasi, dan validitas

**Desain:** controlled benchmarking and evaluation-audit study dengan frozen identity probes.

**Pertanyaan dari kontrak:** to what extent do sequence condition, non-face contextual information, and temporal frame redundancy alter measured synthetic thermal face identity-representation performance on ThermVision-DB when the identity encoder is frozen and ThermVision identities are used only for evaluation?

**Kontribusi:** audit reliabilitas pengukuran; bukan model baru, SOTA accuracy competition, synthetic generation method, atau validasi eksternal. Pergeseran novelty adalah pertanyaan evaluasi, bukan menambah model/dataset untuk mengalahkan literatur.

**Populasi:** seluruh 50 identitas sintetis dievaluasi. Tidak ada fitting pada ThermVision dan tidak ada split train/test internal. Draft lama 40/10, 30/10/10, 5 folds, atau 3 training seeds bukan desain final Paper 1. Pretraining disjointness terhadap semua kemungkinan identitas sumber tidak diaudit/dibuktikan.

**Semantik:** Set 1/Set 2 merupakan shared sequence/condition templates. Gunakan cross-sequence atau cross-condition, bukan independent acquisition-session generalization. Semua identitas sudah dilihat hasilnya; jangan menyebutnya untouched holdout pada Paper 2/3.

**Batas kausal:** A/B/C adalah kontrol terarah di sekitar referensi bersama, bukan full factorial. Tidak ada estimasi seluruh interaksi. B2-G mendeskripsikan geometry; C mengubah coverage bersama komposisi pose/ekspresi/kualitas. Dua checkpoint mengubah weights, data pretraining, dan detail backbone sekaligus. [S0 bagian 3, 8-11; S4 bagian 1, 11-13]

## 4. Angka desain dan corpus yang terkunci sebelum hasil

| Parameter | Nilai |
| --- | --- |
| Identitas sintetis | 50 |
| Label sex corpus | 25 M + 25 F; bukan demografi partisipan manusia |
| Canonical videos | 100; 2 per identitas |
| Resolusi/FPS | 512 x 512; 30 fps |
| Set 1 | 354 frame/video; 17.700 total; shared head-pose / D3 |
| Set 2 | 250 frame/video; 12.500 total; shared facial-expression / D19 |
| Total frame | 30.200 |
| Missing bbox dipatch | 77 |
| Multi-detection diselesaikan | 2 |
| Final bbox patch rows | 79 |
| Visual QC groups | 27 |
| Crop-expansion QC | 30 kasus = 26 stress + 4 clean controls |
| Crop factor | 1.20 |
| Input probe / embedding | 112 x 112 x 3 / 512-D |
| Primary B / defensive B | 16 / 8 dan 32 |
| Master seed | 20260920 |
| C2 draws | 20 per video, nested |
| Bootstrap / permutations primer | 10.000 / 100.000 |

[S0 bagian 4-9; keputusan corpus/QC tercatat]. Label identitas asli tidak harus bernomor berurutan 01-25; gunakan manifest/mapping, jangan membuat ulang ID dari rentang angka.

**B2-G bukan angka yang bertentangan:** 30.123 frame semula memiliki label, lalu 77 missing-frame patches melengkapi 30.200. Sesudah 2 multi-detection diganti dengan patch final, sumber per-frame adalah **30.121 raw single-label + 79 final-patch = 30.200**. Jangan menjumlahkan 30.123 + 79. [S2 completion]

## 5. Encoder dan preprocessing yang tidak boleh berubah

### 5.1 Primary ArcFace

- `InsightFace buffalo_l / w600k_r50.onnx`; ResNet-50; training label WebFace600K.
- Checkpoint bytes: **174.383.860**.
- Checkpoint SHA256: `4c06341c33c2ca1f86781dab0e829f88ad5b64be9fba56e56bc9ebdefc619e43`.
- Package buffalo_l SHA256: `80ffe37d8a5940d59a7384c201a2a38d4741f2f3c51eef46ebb28218a7b0ca2f`.
- Tidak ada ThermVision fine-tuning, detector re-localization atau landmark alignment. [S0 bagian 5-6]

### 5.2 Secondary AdaFace - checkpoint freeze sudah selesai

- IR-50 / R50, MS1MV2.
- Original: `adaface_ir50_ms1mv2.ckpt`, **700.286.703 bytes**; SHA256 `234da6ce931f821e0a8e920063dc2091d8122ea46285c159d2f25d3f762fecb3`.
- Derived tensor-only: `adaface_ir50_ms1mv2_model_state_dict_only_v1.pt`, **174.654.913 bytes**, **467 tensor keys**; SHA256 `17bb2e4679be9552458a860a967585a27876c4dee0a146299a50909095db90a2`.
- Derived weights telah diuji `weights_only=True` pada freeze run. Jangan membuat ulang serialization hanya untuk memperoleh hash baru; bytes keluaran yang frozen adalah acuannya.
- Official source commit: `c60eaa786a42c03444f3df7096dbaf9d57ae010d`; `net.py` SHA256 `b4db4eb0174a385fd29e5f616391b50d443f455990c8b88dcab1f8021af8ba4c`.
- Exact checkpoint dipilih/frozen sebelum outcome E, bukan sebelum semua outcome ArcFace. Jangan menulis bahwa seluruh penelitian tetap outcome-blind hingga E. [D lock block; S3 source/model lock dan completion]

Hash weights di atas adalah **recorded locks**, tidak dihitung ulang dari weights pada handoff ini. Tidak ada model weights dalam bundle.

### 5.3 Transformasi gambar dan template

`validated canonical bbox + final patch -> grayscale -> bbox-centered square factor 1.20 -> median padding -> bilinear 112x112 -> grayscale identik tiga kanal -> normalization -> frozen encoder -> L2 frame -> mean pooling -> L2 template -> cosine`.

Grayscale adalah `Y=round(0.299R+0.587G+0.114B)`. Side square adalah `ceil(max(w_px,h_px)*1.20)`; code E yang dieksekusi memakai origin `floor(center-side/2)`. Jangan menukar implementasi pembulatan/resize ketika menulis ulang metode. Out-of-frame padding memakai median grayscale per frame; bukan asymmetric crop shift.

ArcFace memakai `(pixel-127.5)/127.5`; AdaFace memakai `(pixel/255-0.5)/0.5`. Tiga channel identik membuat urutan RGB/BGR tidak mengubah nilai kanal. Tidak ada pemasangan MTCNN alignment default AdaFace dalam E. Epsilon normalisasi dalam kontrak adalah `1e-12`. [S0; S3 execution source yang tercatat]

Pemilihan crop factor dilakukan melalui QC visual tanpa recognition outcomes. QC tercatat sebagai audit visual asisten, bukan bukti dua annotator manusia atau bounding-box ground truth pixel-perfect. Bila dijelaskan dalam naskah, pengungkapan harus mengikuti proses aktual. [Riwayat final visual QC; S0]

## 6. Kondisi, sampling, dan baseline bersama

| Kode | Definisi yang dipertahankan |
| --- | --- |
| A0 | face-only, strict cross-sequence S1->S2 and S2->S1, uniform B16 |
| A1 | 32 uniform frames per sequence, split by even/odd positions into two disjoint B16 templates; both sequences/directions |
| A2 | first versus second temporal half; 16 uniform frames in each half; defensive |
| B0 | face-only strict cross-sequence uniform B16; same reference as A0/C0 |
| B1 | full grayscale frame resized directly to 112x112, same B16 selection; secondary |
| B2 | replace factor-1.20 face square with frame median, no inpainting; strict cross-sequence B16; context/background-proxy |
| B2-G | xc,yc,w,h,area=w*h; per-video mean and population SD ddof=0; no geometry-only recognition |
| C0 | face-only strict cross-sequence uniform B16; same reference as A0/B0 |
| C1 | face-only strict cross-sequence contiguous B16 |
| C2 | 20 pre-frozen random B16 draws per video, defensive |
| C3 | uniform/contiguous at B8 and B32 only, defensive |
| D | within-versus-between identity geometry diagnostic |
| E | AdaFace IR-50 only A0/A1, B0/B2, C0/C1; no full factorial |

**Sampling:** uniform `rint(linspace(0,N-1,B)).astype(int)`; seed64 berasal dari 8 byte pertama SHA256 string `MASTER_SEED | namespace | canonical_video_id | draw_no`, unsigned big-endian. C1 memakai `start=seed64%(N-B+1)` dengan namespace `C1_CONTIGUOUS`. C2 memakai PCG64, without replacement, lalu indeks diurutkan.

Aturan di atas menjelaskan metode. Untuk reproduksi indeks aktual, **frozen frame plan dan adapter adalah sumber**, bukan menebak kembali separator string, label kondisi, atau ID. A1 membagi posisi even/odd dalam daftar uniform-32, bukan memilih parity nomor frame video.

Alias baseline di ekspor berbeda: ArcFace `A0_C0_B0`, AdaFace `A0_B0_C0`. Keduanya merujuk baseline desain yang sama; bukan kondisi baru. Adapter memakai ID pendek seperti `F_01_S1`, sementara canonical/geometry memakai `F_01_S1_HEADPOSE`. Technical patch E v1.1 menyimpan pemetaan bijektif melalui `(identity_id,set_id)`; jangan join menggunakan exact string pendek ke panjang atau membuat mapping baru. [S0 bagian 7; S1 adapter; S3 namespace map]

## 7. Statistik dan aturan reporting

**Tepat tiga primary hypotheses:** A = A1-A0 margin; B = retrieval B2 melawan gallery-label permutation null; C = C1-C0 margin. A/C memakai paired identity sign-flip dua sisi; B upper-tail. `B1-B0` tetap secondary predeclared.

Unit inferensi adalah **identitas**. Correctness dan margin utama seimbang dua arah; A1/A2 juga seimbang atas dua sekuens. Nilai correctness per identitas boleh 0.5 atau pecahan lain, tetapi itu bukan confidence/probabilitas terkalibrasi. Jumlah arah/template/draw tidak menambah N.

Bootstrap 95% = 10.000 replicates; permutation primer = 100.000. Rank-1 adalah metric pengenalan, genuine-minus-maximum-impostor cosine margin adalah effect statistic. EER sekunder dan ROC-AUC deskriptif; very-low-FAR tidak menjadi endpoint utama.

**Pertahankan output as-exported:** primary p-values adalah raw Monte Carlo; tiga nilai yang diekspor adalah `1/100001 = 9.99990000099999e-06`, bukan p=0 dan bukan bukti family correction yang tidak dilakukan. Holm tersedia pada keluarga secondary margin; exact McNemar B1/B0 dilaporkan per arah sebagaimana ekspor. Jangan menerapkan koreksi baru diam-diam pada tahap writing.

Robustness E memberikan Rank-1/margin/EER/AUC, CI kondisi Rank-1/margin, dan CI paired margin A/B/C. **Tidak ada p-value E**, tidak ada EER CI E di ekspor, dan tidak ada primary paired-effect CI ArcFace pada tabel ekspor. Jangan membuat CI tersebut dengan mengurangi CI kondisi atau menyalin CI encoder lain.

CI degenerat [100%,100%] atau EER [0,0] adalah sifat bootstrap sampel ini, bukan jaminan zero risk eksternal. C2 dekat secara numerik dengan C0, tetapi tidak diuji ekuivalensi. Kontrak adalah internal frozen/predeclared protocol; tidak ada bukti registrasi publik pada paket ini. [S0 statistik; S1; S3; S4 bagian 12]

## 8. Angka hasil yang dibekukan sebagai evidence - bukan target tuning

Angka pada bagian ini adalah hasil yang sudah terlihat dan diekspor. Presisi tampilan diringkas; sumber CSV asli dan `frozen_reported_results` pada JSON mempertahankan locator. Tidak ada tes/CI baru dihitung untuk handoff.

### 8.1 ArcFace: seluruh kondisi pada condition_summary.csv

| Condition | Rank-1 (%) | Margin mean | EER (%) | ROC-AUC |
| --- | --- | --- | --- | --- |
| A0_C0_B0 | 98.0 | 0.2277 | 2.0000 | 0.996824 |
| A1 | 100.0 | 0.2747 | 0.0000 | 1.000000 |
| A2 | 100.0 | 0.2632 | 0.0000 | 1.000000 |
| B1 | 100.0 | 0.2162 | 2.0000 | 0.996776 |
| B2 | 96.0 | 0.1047 | 2.0000 | 0.996539 |
| C1 | 97.0 | 0.1719 | 4.0000 | 0.995110 |
| C3_uniform_B8 | 98.0 | 0.2316 | 2.0000 | 0.995878 |
| C3_contig_B8 | 95.0 | 0.1720 | 4.2653 | 0.994596 |
| C3_uniform_B32 | 99.0 | 0.2307 | 2.0000 | 0.997012 |
| C3_contig_B32 | 94.0 | 0.1970 | 4.0000 | 0.993845 |

[S1/results/condition_summary.csv]. Tabel ini tidak menampilkan ulang seluruh CI. CI kondisi yang tersedia ada pada `bootstrap_ci_required.csv`; jangan menyimpulkan setiap baris C3 mempunyai CI yang diekspor.

### 8.2 Primary dan secondary contrast ArcFace

| Uji | Estimasi | p as-exported | Keterangan |
| --- | --- | --- | --- |
| A1-A0 margin | 0.04701042 | 9.99990000099999e-06 | two-sided |
| B2 Rank-1 vs permutation null | 0.96; null mean 0.0200514 | 9.99990000099999e-06 | upper-tail; null percentiles 0-0.05 |
| C1-C0 margin | -0.05577069 | 9.99990000099999e-06 | two-sided |

| Secondary margin contrast | Estimate | p raw | p Holm |
| --- | --- | --- | --- |
| A2 - A0 margin | 0.03552332 | 9.99990000099999e-06 | 4.9999500004999955e-05 |
| B1 - B0 margin | -0.01153209 | 0.02777972220277797 | 0.02777972220277797 |
| C2(mean 20 draws) - C0 margin | -0.00335071 | 9.99990000099999e-06 | 4.9999500004999955e-05 |
| C3 B=8: contiguous - uniform margin | -0.05950725 | 9.99990000099999e-06 | 4.9999500004999955e-05 |
| C3 B=32: contiguous - uniform margin | -0.03365914 | 0.002059979400205998 | 0.004119958800411996 |

[S1/primary_hypotheses.csv; primary_B_null_summary.csv; secondary_margin_holm.csv]. B1-B0 exact McNemar = 1.0 per arah. C2 rata-rata 20 draw: Rank-1 98.3%, margin sekitar 0.22434; delta margin -0.0033507. Ini mean of draw metrics, bukan skor yang dipool ulang. D: within mean sekitar 0.9362, between mean 0.5029, delta 0.4333. [S1; S4]

### 8.3 AdaFace: empat kondisi bersama dan paired effects

| Condition | Rank-1 (%) | Margin mean | EER (%) | ROC-AUC |
| --- | --- | --- | --- | --- |
| A0_B0_C0 | 98.0 | 0.2175 | 2.0000 | 0.993396 |
| A1 | 100.0 | 0.2805 | 0.0000 | 1.000000 |
| B2 | 99.0 | 0.1129 | 2.0000 | 0.996343 |
| C1 | 74.0 | 0.1257 | 10.1837 | 0.969780 |

| Effect | Estimate | 95% paired bootstrap CI | p |
| --- | --- | --- | --- |
| A1 - A0 | 0.06299981 | [0.05088741, 0.08289194] | tidak dihitung |
| B2 - B0 | -0.10462902 | [-0.12767204, -0.08199514] | tidak dihitung |
| C1 - C0 | -0.09178355 | [-0.12334158, -0.06114948] | tidak dihitung |

[S3/results]. E contrast B2-B0 margin bukan pengulangan primary B terhadap null. Arah temuan kualitatif bertahan, magnitude tidak identik. Penurunan Rank-1 C pada AdaFace = 24 percentage points, bukan penurunan yang sama pada kedua checkpoint.

### 8.4 B2-G, heterogenitas, dan M_21

B2-G menyimpan 30.200 frame / 100 video / 50 identitas. Mean within-video SD Set1 versus Set2: xc 0.03228 vs 0.00126; yc 0.03056 vs 0.00189; w 0.01508 vs 0.00285; h 0.02529 vs 0.00454; area 0.01758 vs 0.00262. Ini agregasi deskriptif 50 SD per set, bukan pooled SD atau uji baru. [S2; S4/T07]

A1-A0 positif pada 50/50 identitas pada kedua checkpoint. C1-C0 negatif pada 38/50 ArcFace dan 37/50 AdaFace; arah efek C sama antarcheckpoint pada 45/50 identitas. Karena sebagian identitas membaik, tulis menurun **secara rata-rata**, bukan untuk seluruh identitas. [S4 bagian 2 dan 6]

M_21 adalah ilustrasi numerik post-outcome, bukan subgroup confirmatory. ArcFace baseline margin identity-balanced -0.0219093, A1 +0.3733796, B2 -0.0815435, C1 +0.0376939. Jadi M_21 justru berhasil pada ArcFace C1. Angka diagnostic satu arah -0.0404762 berasal dari genuine 0.6076929 versus max impostor 0.6481691; jangan menggantikan balanced margin dengan angka satu arah. Pada AdaFace M_21 baseline -0.09568, A1 +0.38213, B2 -0.06150, C1 -0.08628. Tidak ada diagnosis visual kausal dari tabel tersebut dan tidak ada exclusion. [S1; S3; S4/T08]

## 9. Execution-record locks dan cache counts

| Artifact/count | Nilai |
| --- | --- |
| ArcFace face embeddings | 30.200 |
| ArcFace full B16 embeddings | 1.600 |
| ArcFace B2 embeddings | 1.600 |
| AdaFace selected face embeddings | 5.950 = union indeks A0/A1/C1, bukan all-frame cache |
| AdaFace B2 embeddings | 1.600 |
| Canonical E cache records | 100 |
| Embedding index ArcFace SHA256 | fa17cebb55b696e4b257af98d258716bb69b9a234a0eed71c75f149f68e94d74 |
| Frozen frame plan SHA256 | 455b3925c9bee83faba1b58d668985679c9289cf19dcd7e661d4f966d0718d00 |
| Fresh integrity report SHA256 | c3082bf4281392354cbbd0869514e8b2e299d8d806ffa4945124b7b1572d1f67 |
| Confirmatory adapter SHA256 | c64f81cd5dd80444b421af23a23a99366b851af29fe8fc4fda67b06dec3eb796 |
| B2-G frame geometry SHA256 | ef03d96eec0d6e0110d22a2a7d361839901e0b8f7501e1b6207c5085be7cf6d6 |
| E namespace map SHA256 | b240e92abd97cead7dc7f31c563fada8ef86b321eee9f808eb94056d3048e207 |
| E frame request SHA256 | 671dd748b9b80924b491d0c1ce2550642dc3e3abe7b29fd63c2e044fef7b2952 |
| E cache index SHA256 | e5d70a6a7515b2f1a7e388b26f302dc6b02b05750f77d07c8f7e4fd7f189820c |

Hash artifact yang tersedia sebagai ZIP member diverifikasi melalui manifest. Hash raw embeddings/weights atau laporan integrity yang hanya disebut di completion adalah recorded references, bukan klaim raw file diverifikasi kembali. Catatan tanggal completion (UTC): S1 2026-09-21 10:48:11; S2 12:36:27; S3 15:30:02. Handoff dibuat 22 September 2026 dan tidak mengubah timestamp sumber. [S1-S3 metadata]

## 10. Paket, direktori, dan locator bukti

### 10.1 Struktur minimal yang perlu dibaca

```text
sources/Paper1_Final_Evidence_Synthesis_v1.zip
  Paper1_Final_Evidence_Synthesis_v1.md
  Paper1_Final_Evidence_Synthesis_v1.docx
  Paper1_Manuscript_Tables_v1.xlsx
  tables/T01 ... T09
  figures/F01 ... F04 (.png + .svg)
  Figure_Captions.md
  provenance/Reporting_Decisions.md
  provenance/Synthesis_Input_Audit.json
  sources/Paper1_Confirmatory_Results_v1.zip
  sources/Paper1_B2G_Defensive_Results_v2.zip
  sources/Paper1_Robustness_E_AdaFace_Results_v1_1.zip
  sources/Paper1_Handoff_Checkpoint_v1_0_LOCKED.md
```

Baca tiga result ZIP nested sebagai sumber numerik final, bukan hanya README atau completion status. Tidak diperlukan GPU untuk membaca artefak ini.

### 10.2 Pemetaan materi ke sumber

| Kebutuhan | Locator |
| --- | --- |
| Metode sebelum outcome | S0 bagian 3-11; Contract/Config v1.0 yang hash-nya tercatat |
| A/B/C/D dan C3 point estimates | S1/results/condition_summary.csv |
| Primer A/B/C | S1/results/primary_hypotheses.csv dan primary_B_null_summary.csv |
| Secondary margin/McNemar | S1/results/secondary_margin_holm.csv dan secondary_B1_B0.csv |
| CI ArcFace yang tersedia | S1/results/bootstrap_ci_required.csv |
| C2 nested draws | S1/results/C2_draw_results.csv; identity_level_outcomes.csv untuk mean-draw per identity |
| Geometry diagnostic + M_21 | S1/results/identity_geometry_by_identity.csv dan identity_level_outcomes.csv |
| B2-G exact geometry | S2/results/B2G_frame_geometry_30200.csv dan B2G_video_geometry_mean_std_100.csv |
| Robustness E | S3/results/AdaFace_Robustness_E_Condition_Summary.csv, Bootstrap_CI.csv, Key_Contrasts.csv, Identity_Outcomes.csv (semua memakai prefix AdaFace_Robustness_E_) |
| Interpretasi akhir/figure captions | S4/Paper1_Final_Evidence_Synthesis_v1.md dan Figure_Captions.md |

### 10.3 Lokasi persisten yang tercatat, bukan live verification

| Peran | Logical Drive path |
| --- | --- |
| raw_private | `MyDrive/Paper3/raw_cache/ThermVision_DB/` |
| arcface_execution | `MyDrive/Paper3/Paper1_Main_v1_0/` |
| arcface_cache | `MyDrive/Paper3/Paper1_Main_v1_0/embeddings/arcface_w600k_r50_v1/` |
| confirmatory | `MyDrive/Paper3/Paper1_Confirmatory_v1_0/` |
| B2G | `MyDrive/Paper3/Paper1_B2G_Defensive_v2/` |
| AdaFace_freeze | `MyDrive/Paper3/Paper1_AdaFace_IR50_Freeze_v1/` |
| AdaFace_E | `MyDrive/Paper3/Paper1_Robustness_E_AdaFace_v1/` |

Mountpoint historis: `/content/gdrive_p1`. Folder `/content` runtime sementara tidak menjadi otoritas. Live Drive tidak diakses dalam tugas ini; jangan mengklaim bundle telah tersimpan otomatis ke Drive.

Raw archives privat tetap immutable: Male Subjects.zip SHA256 `24d59ed6b1559904089d9e0589c88e7b4945fe50d31ebf108a594f4fccb67318` (sekitar 9.647 GiB), Female Subjects.zip SHA256 `45eccef45dffebd20ed422feb7be86caf6666c0a2dceadd47b28d72a0cddaeea` (sekitar 10.183 GiB). Ukuran adalah angka historis dibulatkan, bukan byte count baru. Jangan redistribusi raw archives atau weights. [S0 bagian 2]

## 11. Technical history dan supersession register

| Item historis | Status sekarang | Tindakan saat resume |
| --- | --- | --- |
| S0: extraction belum complete, confirmatory belum run, AdaFace belum frozen | Superseded oleh S1-S3 dan keputusan closure | Jangan mulai ulang pipeline. |
| Confirmatory v1 gagal membaca label frame plan | Adapter technical patch v1.1 dipakai dalam S1 | Gunakan adapter frozen, bukan tebakan schema. |
| S1 completion: B2G_geometry_cache_not_unique; AdaFace belum dijalankan | Benar pada waktu S1 diekspor; kemudian ditutup oleh S2/S3 | Jangan mengedit S1 agar tampak semua tahap sudah ada sejak awal. |
| B2-G recovery | S2 merekonstruksi geometry dari provenance bbox final | Bukan experiment/classifier geometry baru. |
| AdaFace torch.load Lightning metadata | Freeze technical patch v1.1 menghasilkan tensor-only artifact | Jangan deserialize ulang original checkpoint untuk menulis paper. |
| E v1 ID pendek versus canonical ID panjang | Pemetaan bijektif technical patch v1.1 tersimpan | Gunakan map 100/100 yang ada; jangan membuat ulang namespace. |
| S3 progress = embedding_cache_complete, completion = completed | Minor packaging-order discrepancy tercatat | Pertahankan kedua file; jangan rerun experiment untuk merapikannya. |
| Figure histogram awal D tidak seimbang raw counts | S4 memakai per-query genuine vs max impostor yang tersedia | Tidak ada 2.450 individual impostor scores dalam paket; jangan mengarang density/ECDF. |
| Judul/RQ lama menyebut identity-disjoint train/test | Superseded oleh frozen-probe study | Jangan klaim split lama dijalankan. |
| Rekomendasi jurnal IJBM/CVIU/Elsevier/SIVP | Riwayat screening; MVA kini dipilih pengguna | Jangan kembali screening kecuali diminta. |

`PENDING` dalam ekspor visual-QC awal bukan ACCEPT. Keputusan final tersendiri tercatat sebagai audit visual asisten. Notebook lama yang gagal tetap historis, bukan petunjuk operasional tahap sekarang. [S0-S4; D]

## 12. Target jurnal dan batas finansial

**Target kerja aktif: Machine Vision and Applications (MVA), Springer Nature.** Pengguna memilih mencoba MVA setelah membandingkan IJBM/SIVP dan kandidat Elsevier. Ini bukan submission yang sudah dilakukan dan bukan jaminan acceptance/Q1. Status kuartil tidak dikunci dalam checkpoint ini.

**Anggaran:** pengguna menyatakan tidak mempunyai funding untuk APC. Batas kerja adalah APC 0 dan total biaya wajib 0, tanpa bergantung pada waiver yang belum disetujui. Jalur yang direncanakan adalah subscription/non-OA; halaman resmi MVA menyatakan jalur ini tidak dikenai APC. Pilihan berbayar opsional tidak diambil. Ketentuan aktual diperiksa lagi sebelum menyetujui pembayaran/produksi. Jangan menganggap keterbatasan APC membuktikan seluruh dukungan riset/in-kind tidak ada; kalimat funding final memerlukan konfirmasi penulis. [D; G5]

SIVP/CVIU/IVC hanya opsi historis/cadangan, bukan target paralel aktif. Tidak ada simultaneous submission. Judul final belum dipilih: judul kerja pada S0 dapat menjadi dasar, tetapi boleh dipadatkan untuk pembaca MVA tanpa mengganti RQ, kondisi, atau hasil.

## 13. Panduan penulisan yang telah disepakati

### 13.1 MVA - persyaratan eksternal, bukan scientific locks [G1]

- Abstrak 150-250 kata; 4-6 keywords.
- Sumber editable wajib; LaTeX `iicol` direkomendasikan, Word diterima.
- Heading desimal maksimal 3 tingkat; sitasi numerik kurung siku, DOI bila tersedia.
- Tabel/figure berurutan; caption dalam manuskrip. Warna online gratis, biaya warna cetak perlu dihindari.
- Data Availability Statement wajib; deklarasi relevan dan informasi kontribusi/competing interests di sistem submission.
- LLM bukan penulis; penggunaan substantif diungkapkan, manusia bertanggung jawab.
- Tidak ditemukan batas total halaman eksplisit pada halaman yang diperiksa; jangan diasumsikan tanpa batas.

Panduan resmi diperiksa ulang 22 September 2026. Saat finalisasi, cek artwork, supplementary, hak penggunaan, dan file yang disyaratkan langsung pada halaman resmi; jangan menganggap PNG/SVG internal otomatis format produksi akhir.

### 13.2 Wisconsin - fungsi abstrak [G2]

Abstrak harus dapat dipahami sendiri: konteks/masalah, tujuan, metode, hasil, dan implikasi. Selesaikan sesudah draf utama. Proporsi/jumlah kalimat bukan aturan universal dan ketentuan MVA didahulukan. Target kerja 200-230 kata adalah usulan penyusunan, bukan syarat tambahan jurnal.

Akses: URL assignments pengguna menampilkan pemeriksaan Javascript; halaman academicwriting tidak terbuka langsung pada cek ini, tetapi isi halaman resmi tersedia melalui indeks pencarian. Jangan menyebutnya full direct-page review yang berhasil.

### 13.3 UNC - Related Work sebagai sintesis [G3]

Organisasikan hubungan antargagasan, bukan satu paragraf per paper. Sintesis, seleksi bukti, dan parafrasa akurat lebih penting daripada jumlah sitasi. Rancangan Paper 1 memakai tema: synthetic thermal representation; protocol/sequence dependence; residual contextual information; temporal sampling/template construction. Tema ini pilihan penulisan kita, bukan struktur wajib UNC.

### 13.4 PLOS - respons reviewer nanti, bukan blueprint metode [G4]

Jawab setiap komentar secara langsung dan sopan; bedakan komentar, jawaban, perubahan, serta lokasi revisi. Rule 8 menganjurkan memenuhi permintaan bila memungkinkan dan tidak menjadikan outside scope alasan otomatis. Evaluasi permintaan substantif melalui change control. Tidak ada reviewer comments aktual pada checkpoint ini.

Format kerja nanti: `komentar -> jawaban -> tindakan/perubahan -> lokasi versi revisi -> alasan bila tidak diikuti`.

## 14. Blueprint Manuscript Draft v1 untuk MVA

Blueprint berikut adalah rencana editorial, bukan format yang diwajibkan jurnal atau teks Draft v1 yang sudah selesai.

| Bagian | Tujuan penulisan | Bukti/batas wajib |
| --- | --- | --- |
| Introduction | Jelaskan mengapa performa tinggi belum cukup untuk menafsirkan kemampuan identitas; rumuskan audit | Bukan pengantar panjang semua DL; bukan lomba encoder/SOTA. |
| Related Work | Sintesis empat tema dan bedakan pertanyaan kita dari closest work | Jangan menafsirkan tidak terlihat di abstrak sebagai tidak dilakukan; verifikasi sumber primer. |
| Materials and Evaluation Protocol | Laporkan corpus, sequence semantics, probes, preprocessing, kondisi, metric, statistics | Tidak ada split/fitting ThermVision; salin metode aktual, bukan desain lama. |
| Results | A -> B -> C -> diagnostic/robustness sesuai alur bukti | Point estimates, CI yang tersedia, effect direction, null dan denominator harus jelas. |
| Discussion and Limitations | Gabungkan tiga audit dan implikasi pengukuran | Pisahkan observasi, mekanisme kompatibel, dan klaim belum diuji; pertahankan heterogenitas. |
| Conclusion | Jawab RQ tanpa angka/metode baru | Internal reliability; bukan external thermal biometric validity. |
| Declarations/availability | Isi fakta administratif yang telah dikonfirmasi | Jangan mengarang author metadata, ethics approval, funding, atau akses publik. |

**Urutan kerja:** outline/claim map -> Methods dan Results -> Related Work dan Introduction -> Discussion dan Conclusion -> abstract final -> submission audit. Ini pilihan alur kerja proyek; bukan kewajiban seluruh pedoman.

Naskah untuk MVA disiapkan dalam bahasa Inggris; diskusi/checkpoint operasional tetap bahasa Indonesia. Pilihan DOCX versus LaTeX belum menjadi scientific lock dan dapat ditentukan untuk kemudahan editing. Isi harus stabil sebelum perapihan format akhir.

Materi tesis Paper 2/3 tidak ditambahkan sebagai metode Paper 1. Posisi Paper 1 adalah fondasi evaluasi; ia tidak membuktikan reliability weighting atau adaptive selection yang belum diuji.

## 15. Pekerjaan yang sudah selesai

| Tahap | Status | Basis |
| --- | --- | --- |
| Literature/claim gate | LOCKED | Original handoff and claim-lock records; not a claim that all cited full texts are archived here. |
| Dataset/canonical/visual QC | GREEN / COMPLETE | Original handoff; 27 groups, 79 patches, 30 crop-QC cases. |
| ArcFace/crop/contract freeze | v1.0 LOCKED | Expected hashes in original handoff; raw contract files not rehashed in this handoff. |
| ArcFace extraction | COMPLETE_RECORDED | User completion block and later result metadata: 30200 face, 1600 full, 1600 B2. |
| Fresh-runtime integrity | PASS_RECORDED | Report hash c3082bf... is referenced in S1 completion; original report bytes not rehashed here. |
| Confirmatory A/B/C/D + A2/C2/C3 | COMPLETE | S1 completion/results package. |
| B2-G provenance recovery | COMPLETE | S2 completion/results: 30200 rows, 100 videos, no recognition metric. |
| AdaFace exact checkpoint freeze | LOCKED_RECORDED | User lock block + S3 metadata; no weight file loaded or rehashed here. |
| Robustness E | COMPLETE | S3: key contrasts only, no new p-values; namespace map retained. |
| Final Evidence Synthesis | v1 COMPLETE | S4 package and source text; original evidence preserved. |
| Experimental closure | CLOSED_BY_USER_AGREEMENT | User explicitly agreed execution remains closed. |
| Journal selection | MVA_SELECTED | Latest explicit user selection; not an acceptance guarantee. |
| Writing-guideline review | RECORDED / RECHECKED_2026-09-22 | MVA, Wisconsin, UNC, PLOS; see guideline provenance. |
| This handoff | v2.0 CREATED | New status/manifest checkpoint; not an experiment-contract revision. |

Status COMPLETE merujuk kelengkapan pekerjaan/evidence yang dilaporkan, bukan janji semua penilaian reviewer dapat dijawab tanpa revisi. Status literature gate LOCKED juga tidak menggantikan audit ketepatan sitasi saat menyusun manuskrip.

## 16. Pekerjaan tersisa - hanya penulisan, pelaporan, dan administrasi

| ID | Pekerjaan | Output | Status |
| --- | --- | --- | --- |
| M01 | Bangun kerangka argumen MVA dan source-to-section/claim map | Outline + table/figure/citation map | NEXT |
| M02 | Tulis Methods dan Results dari kontrak serta ekspor hasil | Methods/Results Draft v1 dengan locator sumber | NOT_STARTED |
| M03 | Verifikasi referensi yang benar-benar dipakai; susun Related Work tematik dan Introduction | Bibliography terverifikasi + sintesis literatur | PENDING |
| M04 | Tulis Discussion, Limitations, Conclusion; pertahankan hasil berlawanan dan batas mekanisme | Discussion/Conclusion Draft v1 | PENDING |
| M05 | Tentukan penempatan tabel/figure utama versus supplementary; format ulang tanpa mengganti data | Paket figure/tabel untuk MVA + captions | PENDING |
| M06 | Susun abstrak akhir 150-250 kata, 4-6 keywords, dan judul akhir setelah badan naskah stabil | Abstract/title/keywords v1 | PENDING |
| M07 | Lengkapi informasi penulis, kontribusi, pendanaan, competing interests, data/code availability, etika yang relevan, dan pengungkapan AI sesuai penggunaan aktual | Title page + declarations; memerlukan verifikasi manusia | PENDING_AUTHOR_INFORMATION |
| M08 | Audit klaim-angka-sitasi, reproduksibilitas pelaporan, izin bahan, format MVA, serta biaya non-OA | Pre-submission checklist dan change log | PENDING |
| M09 | Review pembimbing/coauthor, finalisasi sumber editable dan cover letter; submit hanya setelah persetujuan | Submission package MVA | NOT_AUTHORIZED_FOR_SUBMISSION |

Tidak ada pekerjaan di daftar ini yang mengotorisasi model inference, sampling baru, atau hypothesis testing tambahan. Menata ulang tabel, mengonversi format figure, dan mengecek kesamaan angka terhadap ekspor diperbolehkan; menjalankan eksperimen lain bukan pekerjaan formatting.

### Informasi yang masih harus dikonfirmasi sebelum submission

Nama/urutan penulis, afiliasi, corresponding author dan email, ORCID, kontribusi setiap penulis, dukungan pendanaan/in-kind yang sebenarnya, competing interests, kebutuhan/pernyataan etik yang relevan, hak membagikan materi turunan, alamat repository data/kode yang benar-benar tersedia, dan persetujuan seluruh coauthor/pembimbing. Jangan menyamakan tidak ada dana APC dengan pernyataan funding formal yang sudah final.

Judul, abstrak final, jumlah referensi, penempatan main/supplement, format editable, serta cover letter masih terbuka untuk penyusunan. Pilihan editorial ini boleh berubah selama tidak mengubah fakta dan scientific locks.

## 17. DO NOT CHANGE - daftar cek wajib

1. **LOCK-01:** Jangan membuka eksperimen Paper 1 secara rutin; tahap aktif adalah penulisan MVA.
2. **LOCK-02:** Jangan mengubah 50 identitas, 100 video, 30.200 frame atau mapping canonical; jangan memakai recursive MP4 discovery.
3. **LOCK-03:** Jangan mengganti manifest final, patch bbox, keputusan QC, raw archives, frame plan, atau adapter dengan versi draft/reviewed/PENDING.
4. **LOCK-04:** Jangan melatih/fine-tune probe pada ThermVision, mengganti checkpoint, menambah encoder, atau memilih model berdasarkan hasil.
5. **LOCK-05:** Jangan memasukkan detector/landmark alignment, mengubah crop 1.20, grayscale, padding, bilinear resize, normalisasi, atau pooling.
6. **LOCK-06:** Jangan mengubah B16, defensive B8/B32, master seed, indeks sampling, jumlah draw, atau jumlah bootstrap/permutation.
7. **LOCK-07:** Jangan menambah hipotesis primer keempat; B1-B0 tetap sekunder; B2-null berbeda dari B2-B0 margin pada E.
8. **LOCK-08:** Jangan menghitung p-value E, CI baru yang tidak diekspor, subgroup test, classifier geometry, atau contrast baru sebagai bagian penulisan biasa.
9. **LOCK-09:** Jangan menyebut frame, pair score, arah, seed, draw, atau fold sebagai subjek independen; unit inferensi tetap identitas.
10. **LOCK-10:** Jangan mengklaim split 40/10, 30/10/10 atau identity-disjoint internal telah dijalankan; tidak ada fitting/split internal.
11. **LOCK-11:** Jangan menyatakan disjointness seluruh pretraining telah dibuktikan atau menyebut 50 identitas ini belum pernah dilihat hasilnya.
12. **LOCK-12:** Jangan menyebut Set 1/Set 2 sesi akuisisi independen, real-sensor validation, real-population validity, atau synthetic-to-real generalization.
13. **LOCK-13:** Jangan mengubah context-proxy menjadi background murni; B2-G bukan bukti geometry confounding dihilangkan.
14. **LOCK-14:** Jangan mengatribusikan efek C hanya pada redundancy atau perbedaan E hanya pada loss/arsitektur; mekanisme belum terisolasi.
15. **LOCK-15:** Jangan menghapus identitas/frame yang sulit, mengganti M_21, atau menyembunyikan arah efek yang tidak mengikuti rerata.
16. **LOCK-16:** Jangan menyebut same-sequence effect sebagai train/test leakage tanpa bukti; gunakan protocol/sequence dependence.
17. **LOCK-17:** Jangan menulis p=0, mengubah p mentah menjadi p-adjusted, mengurangi dua CI kondisi untuk membentuk CI paired effect, atau menganggap CI degenerat menjamin generalisasi sempurna.
18. **LOCK-18:** Jangan mengklaim C2 ekuivalen secara formal dengan C0, penambahan frame selalu memperbaiki hasil, atau semua identitas menurun pada C1.
19. **LOCK-19:** Jangan mengklaim interaksi faktorial yang tidak diuji; A/B/C adalah audit terarah di sekitar baseline bersama.
20. **LOCK-20:** Jangan menyamakan PASS manifest dengan audit ulang inference, validitas metode universal, atau jaminan penerimaan/Q1.
21. **LOCK-21:** Jangan menyebut protokol publicly preregistered tanpa bukti registrasi; yang diketahui adalah internal frozen/predeclared contract.
22. **LOCK-22:** Jangan menimpa file hasil, metadata, progress atau synthesis v1; setiap revisi/correction harus berversi dan tertelusur.
23. **LOCK-23:** Jangan mengarang metadata referensi, hasil full-text audit, penulis, afiliasi, ORCID, approval etik, competing interests, atau URL repository.
24. **LOCK-24:** Jangan mengemas raw ThermVision archives, model weights, kredensial, atau menyebut Drive privat sebagai repository publik.
25. **LOCK-25:** Jangan memilih jalur OA/layanan berbayar atau bergantung pada waiver yang belum disetujui; anggaran biaya wajib tetap 0.
26. **LOCK-26:** Jangan membuka kembali screening jurnal tanpa alasan/permintaan; MVA adalah target kerja yang dipilih pengguna.
27. **LOCK-27:** Jangan mencampurkan metode trainable Paper 2 atau selector/latency Paper 3 ke kontribusi Paper 1.
28. **LOCK-28:** Jangan menolak koreksi kesalahan validitas hanya demi mempertahankan penutupan; gunakan change control, bukan overwrite atau eksplorasi tersembunyi.

## 18. Change control dan penanganan kekurangan

**A. Revisi editorial:** bahasa, urutan argumentasi, judul, captions, penempatan tabel, atau format. Boleh dilakukan dalam versi manuskrip baru dengan sumber angka tetap sama.

**B. Koreksi packaging/provenance:** label, locator, atau ketidaksesuaian status yang tidak mengubah hasil. Catat sebagai erratum/addendum, pertahankan file asli. Tidak perlu rerun untuk menghapus riwayat.

**C. Dugaan kesalahan validitas/hasil:** hentikan klaim yang terdampak; simpan bukti dan sumber asli; jelaskan error, ruang lingkup, dan outcome yang sudah terlihat; minta keputusan penulis atas koreksi terencana; keluarkan artifact berversi baru dan comparison log. Jangan menyebut analisis pasca-hasil sebagai predeclared jika bukan. Keputusan closure tidak mengalahkan integritas ilmiah.

**D. Permintaan reviewer substantif:** belum ada pada checkpoint ini. Nilai apakah bisa dijawab dengan evidence yang sudah tersedia, revisi penjelasan, atau membutuhkan pekerjaan baru. Bila perlu pekerjaan baru, pengguna/penulis memutuskan secara eksplisit dengan protokol koreksi/addendum terpisah. Tidak ada otorisasi eksperimen otomatis dari dokumen ini.

**E. File sumber tidak ditemukan:** gunakan file registry dan sumber asli yang tersedia; tandai status unavailable/unverified secara tepat. Jangan menyusun ulang file LOCKED agar hash seolah-olah sesuai atau memakai draft lama. Jangan mengasumsikan file hilang dari Drive hanya karena belum ada di runtime.

**F. Literatur baru/metadata belum pasti:** verifikasi referensi yang diperlukan untuk klaim tulisan. Jangan memperluas scope eksperimen untuk mengejar novelty. Jika literatur benar-benar mengubah kelayakan klaim, catat dan sesuaikan klaim secara terbuka, bukan mengarang perbedaan.

## 19. Gate sebelum menyebut Draft v1 siap direview

- [ ] Setiap angka Results dapat ditelusuri ke filename/row/condition dalam S1-S3 atau tabel sintesis bersumber.
- [ ] Tidak ada perbedaan definisi baseline, arah, margin, atau persen versus percentage points.
- [ ] Tidak ada klaim split/training/causal mechanism/external validity yang tidak dijalankan.
- [ ] Keterbatasan B2/B2-G, sampling C, dua checkpoint, shared templates, dan N=50 tetap terlihat.
- [ ] Semua p-value/CI diberi jenis dan estimand yang benar; CI yang tidak tersedia tidak diciptakan.
- [ ] M_21 dan variasi arah efek tidak dihapus; tidak ada diagnosis visual tanpa evidence.
- [ ] Related Work berupa sintesis dengan reference metadata yang diverifikasi; conference foundational tidak dibuang otomatis.
- [ ] Title/abstract/conclusion menjawab pertanyaan yang sama dan tidak mempromosikan architecture novelty.
- [ ] Author facts/declarations belum terkonfirmasi ditandai, bukan ditebak; penggunaan AI substantif dilaporkan secara akurat.
- [ ] Pedoman MVA dan jalur biaya nol diperiksa sebelum submission; tidak ada jurnal paralel.
- [ ] Raw dataset/weights/credentials tidak dibundel sebagai supplementary.
- [ ] Draft diberi versi, change log, sumber editable, dan persetujuan manusia sebelum submit.

## 20. Resume command untuk chat/researcher berikutnya

Salin perintah berikut bersama file handoff. Attach bundle jika konteks/sumber pada chat baru belum tersedia.

```text
Lanjutkan Paper 1 dari Paper1_Handoff_Checkpoint_v2_0_MVA_WRITING_LOCKED.md
beserta JSON dan bundle sumbernya. Scientific contract tetap v1.0 LOCKED.
Eksperimen Paper 1 sudah CLOSED: ArcFace A/B/C/D, A2/B2-G/C2/C3, dan
AdaFace Robustness E selesai. Semua outcome sudah terlihat. Jangan
menjalankan ulang extraction, menambah kondisi/model/uji, atau kembali
menscreen jurnal.

Target kerja adalah Machine Vision and Applications (MVA), jalur
subscription/non-OA, APC dan anggaran biaya wajib 0, tanpa asumsi waiver.
Final Evidence Synthesis v1 adalah basis penulisan; CSV dalam tiga ZIP
hasil asli menjadi otoritas angka. Kontrak/config v1.0 mengatur metode;
handoff v2.0 hanya memperbarui status dan langkah selanjutnya.

Tugas pertama: susun kerangka argumentasi MVA dan source-to-section map,
lalu mulai Manuscript Draft v1 dari Methods dan Results. Terapkan pedoman
MVA, UW-Madison untuk abstrak, UNC untuk sintesis literatur, dan PLOS untuk
respons reviewer ketika diperlukan. Jangan mengklaim Draft v1 sudah ada.

Pertahankan cross-sequence, context-proxy, identity-level inference,
N=50, tanpa fitting/split train-test internal, tanpa external biometric
validity. Primary B-null bukan E B2-B0 margin. E tidak mempunyai p-value
baru. Jangan menambah CI yang tidak diekspor atau menimpa artifact asli.
Verifikasi sumber sitasi; metadata penulis/deklarasi yang belum tersedia
harus ditandai. Koreksi validitas yang nyata memerlukan change control,
bukan penyembunyian atas nama freeze.
```

## 21. Sumber, batas akses, dan pembacaan awal

| ID | Sumber/locator | Fungsi |
| --- | --- | --- |
| S0 | `sources/Paper1_Handoff_Checkpoint_v1_0_LOCKED.md` | Metode/expected hashes; operational state lama superseded. |
| S1 | `Paper1_Confirmatory_Results_v1.zip`, standalone dan nested dalam S4 | Angka/metadata ArcFace. |
| S2 | `Paper1_B2G_Defensive_Results_v2.zip`, nested dalam S4 | Geometry/provenance defensif. |
| S3 | `Paper1_Robustness_E_AdaFace_Results_v1_1.zip`, nested dalam S4 | E outcomes, mapping, source/checkpoint metadata. |
| S4 | `sources/Paper1_Final_Evidence_Synthesis_v1.zip` dan salinan MD | Sintesis, tabel/figure, reporting decisions, tiga hasil asli. |
| D | Percakapan terbaru: closure disepakati; APC 0; MVA dipilih; empat pedoman diminta | Keputusan operasional pengguna. Tidak ada otorisasi submission. |
| L0 | `sources/Scopus_P1_Review.md`, `Scopus_P1_Literature_Matrix.csv` | Mapping awal historis; bukan otoritas metode final. |
| H0 | `sources/Continue Paper Execution.txt` | Salinan riwayat parsial; jangan menganggap seluruh percakapan terbaru tercakup. |

Pedoman eksternal, dicek 22 September 2026:

- G1: https://link.springer.com/journal/138/submission-guidelines
- G2 (URL pengguna): https://writing.wisc.edu/handbook/assignments/writing-an-abstract-for-your-research-paper
- G2 (halaman resmi terindeks): https://writing.wisc.edu/handbook/academicwriting/writing-an-abstract-for-your-research-paper/
- G3: https://writingcenter.unc.edu/tips-and-tools/literature-reviews/
- G4: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005730#sec006
- G5: https://link.springer.com/journal/138/how-to-publish-with-us

Pedoman eksternal dapat berubah; tanggal pemeriksaan bukan freeze kebijakan penerbit. Ringkasan singkatnya tidak menggantikan halaman resmi. Tidak ada penambahan pencarian jurnal/literatur luas pada tugas handoff ini.

**Batas verifikasi:** source packages dan nested byte identity diperiksa pada handoff ini; raw data, original model weights, dan live Drive tidak diperiksa. Raw Contract/Config/Claim-Matrix final mempunyai expected hash historis tetapi tidak disalin sebagai file rekonstruksi. Seluruh file yang dibuat handoff ini terdaftar pada manifest baru; tidak ada file sumber yang diubah.

## 22. Pernyataan penutup checkpoint

**Penelitian bukan dimulai ulang.** Handoff ini mengalihkan pekerjaan dari hasil yang sudah selesai menuju manuskrip MVA. Kontribusi tetap audit reliabilitas internal; hasil tetap apa adanya; keputusan penutupan tetap berlaku. Format dan narasi boleh disempurnakan. Klaim dan provenance tidak boleh direkayasa.
