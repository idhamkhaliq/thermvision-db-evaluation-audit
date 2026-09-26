# Release notes - v0.1.0

Initial public reproducibility release accompanying the manuscript:

**Protocol Sensitivity in Synthetic Thermal Video Face Recognition: An Evaluation Audit of ThermVision-DB**

## Included

- frozen ArcFace confirmatory result exports;
- frozen AdaFace IR-50 robustness result exports;
- B2-G geometry summaries;
- crop-QC metadata;
- provenance and SHA256 manifests;
- repository-integrity and reported-result verification scripts;
- ThermVision-DB access/provenance documentation.

## Excluded by design

- raw ThermVision-DB media and upstream annotations;
- ArcFace/AdaFace pretrained model weights;
- credentials or access tokens;
- original execution notebooks whose hashes are documented but whose original
  bytes are not available in the active project file surface.

## Verification boundary

This release supports verification of the reported frozen outputs. It does not
claim that the repository alone can regenerate all embeddings from raw video.

## License

Project-controlled software is released under the MIT License. Upstream data
and third-party model weights retain their own licenses and terms.
