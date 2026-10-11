import typing
import random

typing.Generator
random.*
next()
range()
len()
print()

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["Uno", "Dos", "Tres", "Quatro"]
    actions = ["run", "jump", "hug", "pumch", "kick"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_evemt(
    event: list[tuplle[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)

def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for index in range(1000):
        name, action = next(stream)
        print(f"Event{index}: Plater{name} did action {action}")

    events: list[tuple[str, str]] = []
    for index in range(10):
        events.append(next(stream))
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")

if __name__ == "__main__":
    main()
    
    




