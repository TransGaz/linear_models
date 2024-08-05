import time
import functools

def benchmark_old(func):
    """Выводит время выполнения декорируемой функции"""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() 
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Функция {func.__name__}() выполнена за {run_time:.4f} c")
        return value
    return wrapper


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):      
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)      
        print(f"Была вызвана функция {func.__name__} с параметрами: ({signature})")
        value = func(*args, **kwargs)
        print(f" Функция {func.__name__!r} возвращает {repr(value)}")        
        return value

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
     
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        print(f" Функция {func.__name__}() была вызвана {wrapper.num_calls} of раз!")
        return func(*args, **kwargs)
    wrapper.num_calls = 0
    
    return wrapper

def memo(func):

  """Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми"""
  
  cache ={}

  @functools.wraps(func)
  def fmemo(*args, **kwargs):
      memo_key = args + tuple(kwargs.items())
      if memo_key not in fmemo.memo:
          fmemo.memo[memo_key] = func(*args, **kwargs)
      return fmemo.memo[memo_key]
      fmemo.memo = cache
      return fmemo		
	  
def benchmark(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(func, 'called'):
            func.called = True
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        else:
            result = func(*args, **kwargs)
        return result