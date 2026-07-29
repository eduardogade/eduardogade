
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any, Final



ChromeOptions chromeOptions = new ChromeOptions();

chromeOptions.AddArgument(@"--user-data-dir=" + ChromeProfileUtilities.ProfilePath);
chromeOptions.AddArgument("--profile-directory=Default");


if ((bool)RunParams.IsHeadless)
{
    chromeOptions.AddArgument("--headless=new");
}

var service = ChromeDriverService.CreateDefaultService();
service.HideCommandPromptWindow = true;

driver = new ChromeDriver(service, chromeOptions);
driver.Navigate().GoToUrl("https://google.com");

if (!(bool)RunParams.IsHeadless)
{
    driver.Manage().Window.Maximize();
}
else if ((bool)RunParams.IsHeadless)
{
    driver.Manage().Window.FullScreen();
}
