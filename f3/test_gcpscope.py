import pytest

from gcpscope import classify


@pytest.mark.parametrize(
    ("identifier", "expected_tag"),
    [
        ("gce_vm", "zonal"),
        ("zonal_pd", "zonal"),
        ("cloud_run", "regional"),
        ("us-central1-a", "zone"),
        ("us-central1", "region"),
        ("US", "multi-region"),
        ("nam4", "dual-region"),
    ],
)
def test_classify_known_identifiers(identifier, expected_tag):
    assert classify(identifier) == expected_tag


def test_classify_rejects_unknown_identifier():
    with pytest.raises(ValueError):
        classify("made-up-scope")
