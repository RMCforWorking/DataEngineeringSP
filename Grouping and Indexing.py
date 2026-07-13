employees = [
 {'name':'Alice', 'dept':'Engineering', 'salary':85000, 'manager':'Carol'},
 {'name':'Bob', 'dept':'Marketing', 'salary':52000, 'manager':'Dave'},
 {'name':'Carol', 'dept':'Engineering', 'salary':95000, 'manager':'Eve'},
 {'name':'Dave', 'dept':'Marketing', 'salary':61000, 'manager':'Eve'},
 {'name':'Frank', 'dept':'Engineering', 'salary':38000, 'manager':'Carol'},
 {'name':'Grace', 'dept':'Support', 'salary':41000, 'manager':'Dave'},
]


def deptIndex():
    dept_index = {}
    for emp in employees:
        dept_index.setdefault(emp['dept'], []).append(emp['name'])
    print(f"Dept index: {dept_index}")
    return dept_index


def salaryBracket():
    salary_bracket = {'junior': [], 'mid': [], 'senior': []}
    for emp in employees:
        salary = emp['salary']
        if salary < 40000:
            bracket = 'junior'
        elif salary <= 70000:
            bracket = 'mid'
        else:
            bracket = 'senior'
        salary_bracket[bracket].append(emp['name'])
    print(f"\nSalary bracket: {salary_bracket}")
    return salary_bracket


def highestAvgDept():
    dept_totals = {}
    dept_counts = {}
    for emp in employees:
        dept = emp['dept']
        dept_totals[dept] = dept_totals.get(dept, 0) + emp['salary']
        dept_counts[dept] = dept_counts.get(dept, 0) + 1

    dept_avg = {}
    for dept in dept_totals:
        dept_avg[dept] = dept_totals[dept] / dept_counts[dept]

    best_dept = max(dept_avg, key=dept_avg.get)
    print(f"\nMedii pe departament: {dept_avg}")
    print(f"Departamentul cu cea mai mare medie: {best_dept} ({round(dept_avg[best_dept], 2)})")
    return best_dept


def sameManager():
    manager_index = {}
    for emp in employees:
        manager_index.setdefault(emp['manager'], []).append(emp['name'])

    print("\nAngajati grupati dupa manager:")
    for manager, names in manager_index.items():
        if len(names) > 1:
            print(f"{manager} -> {names}")

    return manager_index


def nameLookup():
    lookup = {}
    for emp in employees:
        lookup[emp['name']] = emp
    print(f"\nLookup nume -> record: {lookup}")
    return lookup


if __name__ == '__main__':
    deptIndex()
    salaryBracket()
    highestAvgDept()
    sameManager()
    nameLookup()