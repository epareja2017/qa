from steps.actionwords import Actionwords

def before_all(context):
   pass

def before_scenario(context, scenario):
   context.actionwords = Actionwords()

def after_all(context):
   pass
