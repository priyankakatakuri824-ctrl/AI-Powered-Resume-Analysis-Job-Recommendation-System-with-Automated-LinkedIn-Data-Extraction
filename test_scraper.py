from backend.scraper import linkedin_login, scrape_jobs

print("🚀 Starting test...")
driver = linkedin_login()

jobs = scrape_jobs(driver, "Python Developer", "Hyderabad")

print("\n📌 Top Job Matches:")
for job in jobs:
    print(f"• {job['title']} - {job['company']}")
    print(f"🔗 {job['link']}\n")

driver.quit()
print("🎯 Test Completed!")
