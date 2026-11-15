"""Tests for host-side audio feature processing."""

from software.src.dsp_pipeline import DSPPipeline


def test_pipeline_stores_sample_rate() -> None:
    pipeline = DSPPipeline(sample_rate_hz=16000)
    assert pipeline.sample_rate_hz == 16000
