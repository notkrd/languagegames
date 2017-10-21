from django.shortcuts import get_object_or_404
from lindenmayergardens.models import Lrule, Lsystem

def StrToLrules(raw_lrule_str):
    """Input a string, and return a list of pairs of strings giving the corresponding L-rules."""
    return filter(lambda llist: len(llist) == 2,
        map(lambda lstr: lstr.split('>', 1),
                     raw_lrule_str.splitlines()))

def ParseLrules(raw_lrule_str, new_lsys):
    """Parse a string into a list of L-rules, using spaces and newlines as separators."""
    lrules = StrToLrules(raw_lrule_str)
    lrule_priority = 0
    for a_rule in lrules:
        Lrule.objects.create(lsys = new_lsys,
                                          str_in=a_rule[0],
                                          str_out=a_rule[1],
                                          rule_priority=lrule_priority)
        lrule_priority += 1

def LrulesToStr(an_lsys_key):
    lrules_str = ""
    for a_rule in Lrule.objects.filter(lsys = an_lsys_key).order_by('rule_priority'):
        lrules_str += '%s > %s \r\n' % (a_rule.str_in.strip(), a_rule.str_out.strip())
    return lrules_str

def UpdateWithRules(text_in_list, rules_as_lists):
    updated_text = []
    while len(text_in_list) >= 1:
        found_match = False
        for a_rule in rules_as_lists:
            if text_in_list[:len(a_rule[0])] == a_rule[0]:
                updated_text += a_rule[1]
                text_in_list = text_in_list[len(a_rule[0]):]
                found_match = True
                break
        if not found_match:
            updated_text.append(text_in_list[0])
            text_in_list = text_in_list[1:]
    return updated_text

    
def IterateUpdateLsys(num_iterations, text_in_list, rules_as_lists):
    for i in range(1, num_iterations):  # @UnusedVariable
        text_in_list = UpdateWithRules(text_in_list, rules_as_lists)
    return text_in_list

def TextList(an_lsys_key):
    an_lsys = get_object_or_404(Lsystem, pk=an_lsys_key)
    return an_lsys.init_text.strip().split()

def RulesList(an_lsys_key):
    an_lsys = get_object_or_404(Lsystem, pk=an_lsys_key)
    def rules_list(a_rule):
        return (a_rule.str_in.strip().split(), a_rule.str_out.strip().split())
    return [rules_list(a_rule) for a_rule in an_lsys.lrule_set.all().order_by('rule_priority')]
    
def format_str_list(an_str_list):
    return " ".join(an_str_list)

def IterateUpdateLsysList(num_iterations, text_in_list, rules_as_lists):
    lsys_stages = [format_str_list(text_in_list)]
    for i in range(1, num_iterations):  # @UnusedVariable
        text_in_list = UpdateWithRules(text_in_list, rules_as_lists)
        lsys_stages.append(format_str_list(text_in_list))
    return lsys_stages
    
def IterateUpdateLsysKey(an_lsys_key, num_iterations):
    a_text_in_list = TextList(an_lsys_key);
    some_rules_as_lists = RulesList(an_lsys_key);
    an_str_list = IterateUpdateLsys(num_iterations, a_text_in_list, some_rules_as_lists)
    return format_str_list(an_str_list)

def IterateUpdateLsysKeyList(an_lsys_key, num_iterations):
    a_text_in_list = TextList(an_lsys_key);
    some_rules_as_lists = RulesList(an_lsys_key);
    an_str_list = IterateUpdateLsysList(num_iterations, a_text_in_list, some_rules_as_lists)
    return an_str_list