# When you import a directory but you havent given a specific file name then it will import __init__.py by default


from controllers.user_controller import user                 # Importing the user blueprint
from controllers.profile_controller import profiles          # Importing the profile blueprint

registerable_controllers = [
    user,
    profiles
]
