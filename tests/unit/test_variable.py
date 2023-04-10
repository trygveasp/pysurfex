"""Test variable."""
from datetime import datetime, timedelta

import pytest

from surfex.variable import Variable


@pytest.fixture(scope="module")
def fixture():
    cfg = {
        "grib1": {
            "fcint": 10800,
            "offset": 0,
            "timestep": 3600,
            "parameter": -1,
            "type": 105,
            "level": 0,
            "tri": 0,
            "prefer_forecast": True,
            "filepattern": "archive/@YYYY@/@MM@/@DD@/@HH@/fc@YYYY@@MM@@DD@@HH@_@LLL@grib_fp",
            "blueprint": {
                "0": "archive/2019/11/13/00/fc2019111300_000grib_fp",
                "1": "archive/2019/11/13/00/fc2019111300_001grib_fp",
                "2": "archive/2019/11/13/00/fc2019111300_002grib_fp",
                "3": "archive/2019/11/13/00/fc2019111300_003grib_fp",
                "4": "archive/2019/11/13/03/fc2019111303_001grib_fp",
                "5": "archive/2019/11/13/03/fc2019111303_002grib_fp",
                "6": "archive/2019/11/13/03/fc2019111303_003grib_fp",
                "7": "archive/2019/11/13/06/fc2019111306_001grib_fp",
                "8": "archive/2019/11/13/06/fc2019111306_002grib_fp",
                "9": "archive/2019/11/13/06/fc2019111306_003grib_fp",
                "10": "archive/2019/11/13/09/fc2019111309_001grib_fp",
            },
            "blueprint_previous": {
                "1": "archive/2019/11/13/00/fc2019111300_000grib_fp",
                "2": "archive/2019/11/13/00/fc2019111300_001grib_fp",
                "3": "archive/2019/11/13/00/fc2019111300_002grib_fp",
                "4": "archive/2019/11/13/03/fc2019111303_000grib_fp",
                "5": "archive/2019/11/13/03/fc2019111303_001grib_fp",
                "6": "archive/2019/11/13/03/fc2019111303_002grib_fp",
                "7": "archive/2019/11/13/06/fc2019111306_000grib_fp",
                "8": "archive/2019/11/13/06/fc2019111306_001grib_fp",
                "9": "archive/2019/11/13/06/fc2019111306_002grib_fp",
                "10": "archive/2019/11/13/09/fc2019111309_000grib_fp",
            },
        },
        "grib2": {
            "fcint": 21600,
            "offset": 10800,
            "timestep": 3600,
            "discipline": 0,
            "parameterCategory": 0,
            "parameterNumber": 0,
            "levelType": 0,
            "level": 0,
            "typeOfStatisticalProcessing": 0,
            "prefer_forecast": True,
            "filepattern": "archive/@YYYY@/@MM@/@DD@/@HH@/fc@YYYY@@MM@@DD@@HH@_@LLL@grib2_fp",
            "blueprint": {
                "0": "archive/2019/11/13/00/fc2019111300_002grib2_fp",
                "1": "archive/2019/11/13/00/fc2019111300_003grib2_fp",
                "2": "archive/2019/11/13/00/fc2019111300_004grib2_fp",
                "3": "archive/2019/11/13/00/fc2019111300_005grib2_fp",
                "4": "archive/2019/11/13/00/fc2019111300_006grib2_fp",
                "5": "archive/2019/11/13/00/fc2019111300_007grib2_fp",
                "6": "archive/2019/11/13/00/fc2019111300_008grib2_fp",
                "7": "archive/2019/11/13/00/fc2019111300_009grib2_fp",
                "8": "archive/2019/11/13/06/fc2019111306_004grib2_fp",
                "9": "archive/2019/11/13/06/fc2019111306_005grib2_fp",
                "10": "archive/2019/11/13/06/fc2019111306_006grib2_fp",
                "11": "archive/2019/11/13/06/fc2019111306_007grib2_fp",
                "12": "archive/2019/11/13/06/fc2019111306_008grib2_fp",
                "13": "archive/2019/11/13/06/fc2019111306_009grib2_fp",
                "14": "archive/2019/11/13/12/fc2019111312_004grib2_fp",
                "15": "archive/2019/11/13/12/fc2019111312_005grib2_fp",
                "16": "archive/2019/11/13/12/fc2019111312_006grib2_fp",
                "17": "archive/2019/11/13/12/fc2019111312_007grib2_fp",
                "18": "archive/2019/11/13/12/fc2019111312_008grib2_fp",
                "19": "archive/2019/11/13/12/fc2019111312_009grib2_fp",
                "20": "archive/2019/11/13/18/fc2019111318_004grib2_fp",
                "21": "archive/2019/11/13/18/fc2019111318_005grib2_fp",
                "22": "archive/2019/11/13/18/fc2019111318_006grib2_fp",
                "23": "archive/2019/11/13/18/fc2019111318_007grib2_fp",
                "24": "archive/2019/11/13/18/fc2019111318_008grib2_fp",
                "25": "archive/2019/11/13/18/fc2019111318_009grib2_fp",
                "26": "archive/2019/11/14/00/fc2019111400_004grib2_fp",
                "27": "archive/2019/11/14/00/fc2019111400_005grib2_fp",
                "28": "archive/2019/11/14/00/fc2019111400_006grib2_fp",
                "29": "archive/2019/11/14/00/fc2019111400_007grib2_fp",
                "30": "archive/2019/11/14/00/fc2019111400_008grib2_fp",
                "31": "archive/2019/11/14/00/fc2019111400_009grib2_fp",
                "32": "archive/2019/11/14/06/fc2019111406_004grib2_fp",
            },
            "blueprint_previous": {
                "0": "archive/2019/11/13/00/fc2019111300_001grib2_fp",
                "1": "archive/2019/11/13/00/fc2019111300_002grib2_fp",
                "2": "archive/2019/11/13/00/fc2019111300_003grib2_fp",
                "3": "archive/2019/11/13/00/fc2019111300_004grib2_fp",
                "4": "archive/2019/11/13/00/fc2019111300_005grib2_fp",
                "5": "archive/2019/11/13/00/fc2019111300_006grib2_fp",
                "6": "archive/2019/11/13/00/fc2019111300_007grib2_fp",
                "7": "archive/2019/11/13/00/fc2019111300_008grib2_fp",
                "8": "archive/2019/11/13/06/fc2019111306_003grib2_fp",
                "9": "archive/2019/11/13/06/fc2019111306_004grib2_fp",
                "10": "archive/2019/11/13/06/fc2019111306_005grib2_fp",
                "11": "archive/2019/11/13/06/fc2019111306_006grib2_fp",
                "12": "archive/2019/11/13/06/fc2019111306_007grib2_fp",
                "13": "archive/2019/11/13/06/fc2019111306_008grib2_fp",
                "14": "archive/2019/11/13/12/fc2019111312_003grib2_fp",
                "15": "archive/2019/11/13/12/fc2019111312_004grib2_fp",
                "16": "archive/2019/11/13/12/fc2019111312_005grib2_fp",
                "17": "archive/2019/11/13/12/fc2019111312_006grib2_fp",
                "18": "archive/2019/11/13/12/fc2019111312_007grib2_fp",
                "19": "archive/2019/11/13/12/fc2019111312_008grib2_fp",
                "20": "archive/2019/11/13/18/fc2019111318_003grib2_fp",
                "21": "archive/2019/11/13/18/fc2019111318_004grib2_fp",
                "22": "archive/2019/11/13/18/fc2019111318_005grib2_fp",
                "23": "archive/2019/11/13/18/fc2019111318_006grib2_fp",
                "24": "archive/2019/11/13/18/fc2019111318_007grib2_fp",
                "25": "archive/2019/11/13/18/fc2019111318_008grib2_fp",
                "26": "archive/2019/11/14/00/fc2019111400_003grib2_fp",
                "27": "archive/2019/11/14/00/fc2019111400_004grib2_fp",
                "28": "archive/2019/11/14/00/fc2019111400_005grib2_fp",
                "29": "archive/2019/11/14/00/fc2019111400_006grib2_fp",
                "30": "archive/2019/11/14/00/fc2019111400_007grib2_fp",
                "31": "archive/2019/11/14/00/fc2019111400_008grib2_fp",
                "32": "archive/2019/11/14/06/fc2019111406_003grib2_fp",
            },
        },
        "netcdf": {
            "fcint": 21600,
            "offset": 10800,
            "timestep": 3600,
            "name": "test",
            "filepattern": "archive/@YYYY@/@MM@/@DD@/meps@YYYY@@MM@@DD@Z@HH@.nc",
            "blueprint": {
                "0": "archive/2019/11/13/meps20191113Z00.nc",
                "1": "archive/2019/11/13/meps20191113Z00.nc",
                "2": "archive/2019/11/13/meps20191113Z00.nc",
                "3": "archive/2019/11/13/meps20191113Z00.nc",
                "4": "archive/2019/11/13/meps20191113Z00.nc",
                "5": "archive/2019/11/13/meps20191113Z00.nc",
                "6": "archive/2019/11/13/meps20191113Z00.nc",
                "7": "archive/2019/11/13/meps20191113Z00.nc",
                "8": "archive/2019/11/13/meps20191113Z00.nc",
                "9": "archive/2019/11/13/meps20191113Z00.nc",
                "10": "archive/2019/11/13/meps20191113Z06.nc",
            },
            "blueprint_previous": {
                "1": "archive/2019/11/13/meps20191113Z00.nc",
                "2": "archive/2019/11/13/meps20191113Z00.nc",
                "3": "archive/2019/11/13/meps20191113Z00.nc",
                "4": "archive/2019/11/13/meps20191113Z00.nc",
                "5": "archive/2019/11/13/meps20191113Z00.nc",
                "6": "archive/2019/11/13/meps20191113Z00.nc",
                "7": "archive/2019/11/13/meps20191113Z00.nc",
                "8": "archive/2019/11/13/meps20191113Z00.nc",
                "9": "archive/2019/11/13/meps20191113Z00.nc",
                "10": "archive/2019/11/13/meps20191113Z06.nc",
            },
        },
        "met_nordic": {
            "fcint": 3600,
            "offset": 0,
            "timestep": 3600,
            "name": "test",
            "accumulated": False,
            "instant": 3600,
            "prefer_forecast": False,
            "filepattern": "archive/@YYYY@/@MM@/@DD@/met_nordic_@YYYY@@MM@@DD@Z@HH@.nc",
            "blueprint": {
                "0": "archive/2019/11/13/met_nordic_20191113Z00.nc",
                "1": "archive/2019/11/13/met_nordic_20191113Z01.nc",
                "2": "archive/2019/11/13/met_nordic_20191113Z02.nc",
                "3": "archive/2019/11/13/met_nordic_20191113Z03.nc",
                "4": "archive/2019/11/13/met_nordic_20191113Z04.nc",
                "5": "archive/2019/11/13/met_nordic_20191113Z05.nc",
                "6": "archive/2019/11/13/met_nordic_20191113Z06.nc",
                "7": "archive/2019/11/13/met_nordic_20191113Z07.nc",
                "8": "archive/2019/11/13/met_nordic_20191113Z08.nc",
                "9": "archive/2019/11/13/met_nordic_20191113Z09.nc",
                "10": "archive/2019/11/13/met_nordic_20191113Z10.nc",
            },
        },
    }
    return cfg


def test_open_new_file_nc(fixture):
    """Test to open a netcdf file."""
    initialtime = datetime(2019, 11, 13, 0)
    intervall = 3600
    case = "netcdf"

    var_dict = fixture[case]
    var_type = case
    for i in range(11):
        validtime = initialtime + timedelta(seconds=intervall * i)
        previoustime = validtime - timedelta(seconds=intervall)
        variable = Variable(var_type, var_dict, initialtime)
        previous_filename = variable.get_filename(validtime, previoustime=previoustime)
        filename = variable.get_filename(validtime)
        assert filename == var_dict["blueprint"][str(i)]
        if i > 0:
            assert previous_filename == var_dict["blueprint_previous"][str(i)]


def test_open_new_file_grib1(fixture):
    """Test to open a grib1 file."""
    initialtime = datetime(2019, 11, 13, 0)
    intervall = 3600
    case = "grib1"

    var_dict = fixture[case]
    var_type = case
    for i in range(11):
        validtime = initialtime + timedelta(seconds=intervall * i)
        previoustime = validtime - timedelta(seconds=intervall)
        variable = Variable(var_type, var_dict, initialtime)
        previous_filename = variable.get_filename(validtime, previoustime=previoustime)
        filename = variable.get_filename(validtime)
        assert filename == var_dict["blueprint"][str(i)]
        if i > 0:
            assert previous_filename == var_dict["blueprint_previous"][str(i)]


def test_open_new_file_grib2(fixture):
    """Test to open a grib2 file."""
    initialtime = datetime(2019, 11, 13, 2)
    intervall = 3600
    case = "grib2"

    var_dict = fixture[case]
    var_type = case
    for i in range(11):
        validtime = initialtime + timedelta(seconds=intervall * i)
        previoustime = validtime - timedelta(seconds=intervall)
        variable = Variable(var_type, var_dict, initialtime)
        previous_filename = variable.get_filename(validtime, previoustime=previoustime)
        filename = variable.get_filename(validtime)
        assert filename == var_dict["blueprint"][str(i)]
        if i > 0:
            assert previous_filename == var_dict["blueprint_previous"][str(i)]


def test_open_new_file_an(fixture):
    """Test to open a met nordic file."""
    initialtime = datetime(2019, 11, 13, 0)
    intervall = 3600
    case = "met_nordic"

    var_dict = fixture[case]
    var_type = case
    if var_type == "met_nordic":
        var_type = "netcdf"
    for i in range(11):
        validtime = initialtime + timedelta(seconds=intervall * i)
        variable = Variable(var_type, var_dict, initialtime)
        filename = variable.get_filename(validtime)
        assert filename == var_dict["blueprint"][str(i)]


def test_open_new_file_fail(fixture):
    """Test failing to open a file."""
    initialtime = datetime(2019, 11, 13, 0)
    case = "met_nordic"
    var_dict = fixture[case]
    var_dict["offset"] = 7200
    var_type = case
    if var_type == "met_nordic":
        var_type = "netcdf"
    with pytest.raises(Exception):
        Variable(var_type, var_dict, initialtime)
