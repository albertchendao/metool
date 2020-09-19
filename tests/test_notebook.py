# -*- coding: utf-8 -*-

import pytest
import datetime
from click.testing import CliRunner
from metool import notebook


def _today():
    d = datetime.date.today()
    return d.strftime('%Y-%m-%d')

def test_ukey():
    runner = CliRunner()
    result = runner.invoke(notebook.ukey)
    assert result.exit_code == 0
    assert len(result.output) == 36 + len('\n')

def test_udate_default():
    runner = CliRunner()
    result = runner.invoke(notebook.udate)
    today = _today()
    assert result.exit_code == 0
    assert result.output == today + '\n'

def test_udate_no():
    runner = CliRunner()
    result = runner.invoke(notebook.udate, 'no')
    assert result.exit_code == 0
    assert result.output == '\n'

@pytest.mark.repeat(10)
def test_udate_random_year():
    runner = CliRunner()
    result = runner.invoke(notebook.udate, 'random-2016')
    assert result.exit_code == 0
    assert result.output.startswith('2016')

@pytest.mark.repeat(10)
def test_udate_random_month():
    runner = CliRunner()
    result = runner.invoke(notebook.udate, 'random-201612')
    assert result.exit_code == 0
    assert result.output.startswith('2016-12')

def test_new_default():
    runner = CliRunner()
    fname = '测试'
    today = _today()
    with runner.isolated_filesystem():
        result = runner.invoke(notebook.new, [fname])
        assert result.exit_code == 0
        assert result.output == 'Successfully create ' + today + ' ' + fname + '.md\n'

@pytest.mark.skip
def test_new_date_no():
    runner = CliRunner()
    fname = '测试'
    with runner.isolated_filesystem():
        result = runner.invoke(notebook.new, [fname, '--date', 'no'])
        assert result.exit_code == 0
        assert result.output == 'Successfully create ' + fname + '.md\n'

def test_deploy():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(notebook.deploy)
        assert result.exit_code == 0
        assert result.output
