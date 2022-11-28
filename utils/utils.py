import os
from typing import Callable, Literal, Tuple, Iterable

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from dotenv import load_dotenv

load_dotenv()

CURRENT_DIR = os.getcwd()
HEADERS = {"cookie": f"session={os.environ['SESSION_COOKIE']}", }


def request_content(year: int, day: int, content_type: str) -> str:
    if content_type == 'input':
        url = f"https://adventofcode.com/{year}/day/{day}/input"
    elif content_type == 'problem':
        url = f"https://adventofcode.com/{year}/day/{day}"
    else:
        raise AttributeError(f'Invalid {content_type = }')

    response = requests.get(url, headers=HEADERS)
    handle_error_status(response.status_code)
    return response.text.strip()


def fetch(year: int, day: int, content_type: str) -> str:
    content = request_content(year, day, content_type)
    if content_type == 'input':
        return content
    elif content_type == 'problem':
        soup = BeautifulSoup(content, "html.parser")
        return '\n\n\n'.join([a.text for a in soup.select('article')])


def fetch_and_save(year: int, day: int, content_type: str) -> None:
    print(f"🛷 Fetching {content_type} for {day} {year}")
    content = fetch(year, day, content_type)
    with open(f"{CURRENT_DIR}/{content_type}", "w") as text_file:
        text_file.write(content)


def load_input(year: int, day: int) -> str:
    for content_type in ['input', 'problem']:
        if not os.path.exists(f"{CURRENT_DIR}/{content_type}"):
            fetch_and_save(year, day, content_type)

    with open(f"{CURRENT_DIR}/input") as file:
        return file.read()


def submit(answer: int, level: int, year: int, day: int) -> None:
    print(f"{Fore.BLUE}📬 Submitting solution now.{Style.RESET_ALL}")
    data = {"level": str(level), "answer": str(answer)}
    response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers=HEADERS, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    message = soup.article.text

    if "that's the right answer" in message.lower():
        print(f"{Fore.GREEN}✅ Correct!{Style.RESET_ALL}")
        save_stars(level)

        if level == 1:
            print("Updated problem with part 2:\n\n")
            print(fetch_and_save(year, day, 'problem'))
    elif "not the right answer" in message.lower():
        print(f"{Fore.RED}❌ Wrong answer! For details:\n{Style.RESET_ALL}")
        print(message)
    elif "answer too recently" in message.lower():
        print(f"{Fore.YELLOW}🚫 You gave an answer too recently{Style.RESET_ALL}")
    elif "already complete it" in message.lower():
        print(f"{Fore.YELLOW}⚠️ You have already solved this.{Style.RESET_ALL}")
        save_stars(level)


def save_stars(level: int) -> None:
    star_path = os.getcwd()
    with open(f"{star_path}/stars", "w+") as star_file:
        stars = '*' * level
        print(f"Writing '{stars}' to star file...")
        star_file.write(stars)


def test(answer_func: Callable[[str], Iterable[int]], cases: list[dict]) -> bool:
    all_passed = True

    if not cases:
        print("Livin' on the edge! No test cases defined.")
        return all_passed

    for tc in cases:
        answer = answer_func(tc['input'])
        if str(tc['output']) == str(answer):
            print(f"{Fore.GREEN}🎄 Test passed {Style.RESET_ALL}[Part {tc['level']}] Input: '{tc['input']}'; Output: '{tc['output']}'")
        else:
            all_passed = False
            print(f"{Fore.RED}🔥 Test failed {Style.RESET_ALL}[Part {tc['level']}] Input: '{tc['input']}'; Submitted: '{answer}'; Correct: '{tc['output']}'")

    return all_passed


def check_stars() -> int:
    star_path = os.getcwd()
    star_file = f"{star_path}/stars"
    if not os.path.exists(star_file):
        return 0

    with open(star_file, 'r') as file:
        stars = file.read().strip()
        return len(stars)


def handle_error_status(code: int) -> None:
    match code:
        case 404:
            print(f"{Fore.RED}{code}: This day is not available yet!{Style.RESET_ALL}")
            quit()
        case 400:
            print(f"{Fore.RED}{code}: Bad credentials!{Style.RESET_ALL}")
            quit()
        case _ if code > 400:
            print(f"{Fore.RED}{code}: General error!{Style.RESET_ALL}")
            quit()


def run(answer_func: Callable[[str], Iterable[int]], test_cases=None):
    year, day = [int(v) for v in CURRENT_DIR.split('/')[-2:]]
    problem_input = load_input(year, day)

    if not test(answer_func, test_cases):
        print("🤷‍♀️ You know the rules. Tests don't pass, YOU don't pass.")
        return

    stars = check_stars()

    print("🍾 Now looking to submit your answers 🍾")
    for part, answer in enumerate(answer_func(problem_input), 1):
        print(f"🧮 Computed answer {answer} for part {part} of day {day}")
        if stars < part:
            submit(answer, part, year, day)
        else:
            print(f"{Fore.BLUE}⏭️ Already solved, skipping submission.{Style.RESET_ALL}")
