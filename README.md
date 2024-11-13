# LuMatch

LuMatch is an AI-powered event recommendation system that matches professionals with relevant AI events (from lu.ma) based on their CV profile. It automatically scrapes events from various sources and creates personalized event schedules.

## Features

- CV Analysis: Reads and analyzes CV content to understand professional background and interests
- Event Scraping: Automatically scrapes AI events from lu.ma/sf
- Smart Matching: Creates personalized event recommendations based on profile analysis
- Formatted Output: Generates clear, markdown-formatted schedules with event relevance explanations

## Prerequisites

- Python 3.9+
- OpenAI API key
- Anthropic API key
- AgentOps API key
- Firecrawl API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rcisneros99/lumatch.git
cd lumatch
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
AGENTOPS_API_KEY=your_agentops_key
FIRECRAWL_API_KEY=your_firecrawl_key
```

4. Place your CV file in `~/data/cv.txt` (LaTeX format supported)

## Usage

Run the main script:
```bash
python src/main.py
```

The script will:
1. Read and analyze your CV from `~/data/cv.txt`
2. Scrape AI events from lu.ma/sf
3. Generate personalized event recommendations based on your profile

## Output Format

The program generates a markdown-formatted output with:
- A brief overview of the most relevant events for your profile
- A detailed schedule of recommended events including:
  - Date and time
  - Event name
  - Brief description
  - Explanation of why each event matches your profile

## Project Structure
```
lumatch/
├── src/
│   ├── config/
│   │   ├── agents.yaml    # Agent configurations
│   │   └── tasks.yaml     # Task definitions
│   ├── tools/
│   │   └── firecrawl_tool.py  # Web scraping tools
│   ├── crew.py            # CrewAI setup
│   └── main.py           # Main execution script
├── .env                  # API keys (not tracked)
└── README.md
```

## Development

This project uses:
- CrewAI for agent orchestration
- OpenAI's GPT-4 for analysis
- Firecrawl for web scraping
- Python-dotenv for environment management

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

Ricardo Cisneros (@rcisneros99)

## Acknowledgments

- CrewAI team for the agent framework
- Lu.ma for providing valuable event data
- AgentStack for making it so easy to build agents!
