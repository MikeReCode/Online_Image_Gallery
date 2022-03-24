from django import template

register = template.Library()


@register.simple_tag()
def format_date(value):
    value = value.split()
    # print("**********", type(value), value)

    try:
        months = {"01": 'January',
                  "02": "February",
                  "03": "March",
                  "04": "April",
                  "05": "May",
                  "06": "June",
                  "07": "July",
                  "08": "August",
                  "09": "September",
                  "10": "October",
                  "11": "November",
                  "12": "December",
                  }

        value = value[0].split(":")
        # print('DATE',f'{value[2]} {months[value[1]]} {value[0]}')

        return f'{value[2]} {months[value[1]]} {value[0]}'
    except:
        return value


@register.simple_tag()
def update_var(value):
    return value
