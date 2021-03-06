import time
WHAT = 'なに'
NAME = 'Jing'

def __based__(number=1, base=20, output=[]):
    factor = number // base
    output = [number % base] + output
    if factor > 0:
        return __based__(factor, base, output)
    return output

def based(number=1, base=20):
    if base < 1:
        return (f"There's no such thing as base {base}.",)
    if base == 1:
        if number > 2**16:
            return (f"That's a whole lot of 1's.",)
        return (1,) * abs(number)
    return __based__(abs(number), base)

def get_input(default, what='number'):
    number = input(f"Type a {what} and hit enter,\nOr just hit enter for {default}: ") or default
    try:
        return abs(int(number))
    except ValueError as e:
        print(f"  Error: {number} is not a decimal number!")
        return None
    
def show_results(number, base, output):
    time.sleep(0.2)
    print("")

    if any([not isinstance(v, int) for v in output]):
        print(f'...{WHAT}?!')
        time.sleep(0.2)
        print(f'Look, {NAME}, we have a problem:')
        print('  '+','.join(map(str,output)))
        return

    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(0.2)
    print("")
    time.sleep(0.2)
    [verb, s] = ['are', 's'] if len(output) > 1 else ['is', '']
    print(f"Here {verb} {number}'s base {base} symbol{s}:")
    print('  '+','.join(map(str,output)))

def main():
    number = get_input(1969)
    if number is None:
        print("")
        time.sleep(0.2)
        return main()
    print(f"  We'll give the digits for {number}.")
    print("")
    time.sleep(0.2)
    base = get_input(20, 'base')
    if base is None:
        print("")
        time.sleep(0.2)
        return main()
    print(f"  We'll use base {base}.")
    output = based(number, base)
    show_results(number, base, output)
    print("")
    time.sleep(1.6)
    return main()

if __name__ == "__main__":
    print(f"\nHello, {NAME}\n")
    main()
