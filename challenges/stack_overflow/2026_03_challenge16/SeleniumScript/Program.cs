using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using System;

class Program
{

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
}
    // static IWebDriver? driver;
    // static dynamic RunParams = new { IsHeadless = false };
    // static string profilePath = @"/Users/egg/Library/Application Support/Google/Chrome";
    // static dynamic ChromeProfileUtilities = new { ProfilePath = profilePath };

    // static void Main()
    // {
    //     ChromeOptions chromeOptions = new ChromeOptions();

    //     chromeOptions.AddArgument(@"--user-data-dir=" + profilePath);
    //     chromeOptions.AddArgument("--profile-directory=Default");

    //     if ((bool)RunParams.IsHeadless)
    //     {
    //         chromeOptions.AddArgument("--headless=new");
    //     }

    //     var service = ChromeDriverService.CreateDefaultService();
    //     service.HideCommandPromptWindow = true;

    //     driver = new ChromeDriver(service, chromeOptions);
    //     driver.Navigate().GoToUrl("https://google.com");

    //     if (!(bool)RunParams.IsHeadless)
    //     {
    //         driver.Manage().Window.Maximize();
    //     }
    //     else if ((bool)RunParams.IsHeadless)
    //     {
    //         driver.Manage().Window.FullScreen();
    //     }

    //     Console.WriteLine("Browser opened successfully!");
    //     Console.ReadLine();
    // }
// }