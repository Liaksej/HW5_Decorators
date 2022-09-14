import datetime
import os


def logger(some_function):
    def decorator(*args, **kwargs):
        with open('logg.txt', 'a') as file:
            wrapped_function = some_function(*args, **kwargs)
            logg_string = f'{datetime.datetime.now()} - {some_function.__name__} - {args, kwargs} - ' \
                          f'{wrapped_function}\n'
            file.write(logg_string)
        print(f'Путь к логам: {os.path.abspath("logg.txt")}')
        return wrapped_function
    return decorator


@logger
def marks_average_finder(name, array):
    for student in array:
        if student == name:
            list_of_marks = array[student]
            average_mark = f'{(float(sum(list_of_marks) / len(list_of_marks))):.2f}'
            return average_mark


if __name__ == '__main__':
    student_marks = {'Krishna': [67, 68, 69],
                     'Arjun': [70, 98, 63],
                     'Malika': [52, 56, 60]
                     }
    query_name = 'Malika'
    print(marks_average_finder(query_name, student_marks))
