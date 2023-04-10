"""Test geometry."""
import json

import pytest

from surfex.cli import cli_set_domain


@pytest.fixture(scope="module")
def domains():
    return {
        "CONF_PROJ_TEST": {
            "nam_pgd_grid": {"cgrid": "CONF PROJ"},
            "nam_conf_proj": {"xlat0": 59.5, "xlon0": 9},
            "nam_conf_proj_grid": {
                "ilone": 1,
                "ilate": 1,
                "xlatcen": 60,
                "xloncen": 10,
                "nimax": 9,
                "njmax": 19,
                "xdx": 10000.0,
                "xdy": 10000.0,
            },
        }
    }


@pytest.fixture(scope="module")
def domains_file(domains, tmp_path_factory):
    fname = f"{tmp_path_factory.getbasetemp().as_posix()}/domains.json"
    with open(fname, mode="w", encoding="utf-8") as fhandler:
        json.dump(domains, fhandler)
    return fname


def test_set_domain(domains, domains_file, tmp_path_factory):
    """Test set domain."""

    saved_domain = domains["CONF_PROJ_TEST"]
    domain_file = f"{tmp_path_factory.getbasetemp().as_posix()}/set_geo_domain.json"
    argv = [
        "-d",
        "CONF_PROJ_TEST",
        "--domains",
        domains_file,
        "-o",
        domain_file,
        "--debug",
    ]
    cli_set_domain(argv=argv)
    with open(domain_file) as fhandler:
        domain_json = json.load(fhandler)
    assert domain_json == saved_domain

    argv = ["-d", "not-existing", "--domains", domains_file, "-o", domain_file, "--debug"]
    with pytest.raises(Exception):
        cli_set_domain(argv=argv)
