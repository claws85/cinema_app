


certificate_age_ranges = (
    ((0, 11), ('U/PG')),
    ((12, 14), ('12')),
    ((15, 17), ('15')),
)

# age = self.calculate_age
# for range in certificate_age_range:
#     lower, upper = range[0]
#     if lower >= age < upper:
#         return range[2]
#         if age >= 18:
#             return '18+'
#         elif 15 >= age < 18:
#             return '15'
#         elif 12 >= age < 15:
#             return '12'
#         else:
#             return 'U/PG'