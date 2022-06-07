def build_profile(first, last, **user_info):
    """Build a user directory with everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile1 = build_profile('albert', 'einstein', 
                                location='princeton', 
                                field='physics')

user_profile2 = build_profile('john', 'lennon', 
                                location='london', 
                                field='music')

user_profile3 = build_profile('warren', 'buffet', 
                                location='omaha', 
                                field='investment')

print(user_profile1)
print(user_profile2)
print(user_profile3)

