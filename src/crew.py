from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool
import os
import tools

@CrewBase
class App1Crew():
	"""app_1 crew"""

	# Agent definitions
	@agent
	def profiler(self) -> Agent:
		cv_path = os.path.expanduser("~/data/cv.txt")
		return Agent(
			config=self.agents_config['profiler'],
			tools=[FileReadTool(file_path=cv_path)],
			verbose=True
		)
	
	@agent
	def scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['scraper'],
			tools=[tools.web_scrape],
			verbose=True
		)
	
	@agent
	def summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['summarizer'],
			tools=[],
			verbose=True
		)
	
	# Task definitions
	@task
	def read_profile(self) -> Task:
		return Task(
			config=self.tasks_config['read_profile']
		)
	
	@task
	def scrape_website(self) -> Task:
		return Task(
			config=self.tasks_config['scrape_website']
		)
	
	@task
	def summarize(self) -> Task:
		return Task(
			config=self.tasks_config['summarize']
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the Test crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)