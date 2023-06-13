function factorial (number) {
    if (isNaN(number) || number <= 1) {
      return 1;
    }
    return number * factorial(number - 1);
  }

  factorial(5)