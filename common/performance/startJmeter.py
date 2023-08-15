# -*- coding: utf-8 -*-
# @Time    : 2022/10/10 06:07
# @Author  : Sara_Jiang
# @name   : Jmeter startup script
# @File    : startJmeter.py
import logging
import os, sys

object_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.split(object_path)
print(file_path)
sys.path.append(file_path[0])
from common.base.path import Base_path

from xml.etree.ElementTree import ElementTree, Element


def get_node_text(node):
    '''
    get node text
    :param node: node
    :return: str
    '''
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)


def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''''Change/add/delete a node's text
      nodelist:node list
      text : updated text'''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


def read_xml(in_path):
    '''Read and parse xml file
      in_path: xml path
      return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def write_xml(tree, out_path):
    '''''write out the xml file
      tree: xml tree
      out_path: write out the path'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def find_nodes(tree, path_xml):
    '''''Find all nodes matching a path
      tree: xml tree
      path_xml: node path'''
    # open xml document
    root = tree.getroot()
    # Find the path which is modified
    sub = root.findall(path_xml)
    return sub


def if_match(node, kv_map):
    '''''Determine if a node contains all incoming parameter attributes
      node: node
      kv_map: A map of attributes and attribute values'''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


def get_node_by_keyvalue(nodelist, kv_map):
    '''''Locate the matching node according to the attribute and attribute value, and return the node
      nodelist: node list
      kv_map: match a map of attributes and attribute values'''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


def jmeter_number(case_name, num_threads, ramp_time, duration, remark, thread_group_name='Thread Group',
                  host_ips='127.0.0.1'):
    '''
    :param case_name: Script name
    :param num_threads: Threads
    :param ramp_time: Control thread step size
    :param duration: Execution time
    :param remark: Comments
    :param host_ips: Load parameters
    :return: Start JMeter successfully
    '''

    if case_name is None:
        return "Test case is empty"
    if num_threads is None:
        return "Virtual concurrency is empty"
    if ramp_time is None:
        return "Test step is empty"
    if duration is None:
        return "Execution time is empty"

    # execute script name
    run_jmeter_file = '%s_%s_%s_%s_%s' % (case_name, num_threads, ramp_time, duration, remark)
    print("execute script name：%s" % run_jmeter_file)
    # thisdir = os.getcwd()

    # original script
    new_dir = os.path.join(Base_path, "test_data/performance", case_name + ".jmx")
    print("current script path: %s" % new_dir)
    if not os.path.exists(new_dir):
        print('Script does not exist! Please check the script')
        return False

    # save test result path
    result_file = os.path.join(Base_path, "test_results/reports", run_jmeter_file)
    print("script execution path: ", result_file)

    # Determine whether the result path exists
    if not os.path.exists(result_file):
        os.makedirs(result_file)
    # 1. read xml file
    doc = read_xml(new_dir)
    # 2. property modification
    # A. find parent node
    nodes = find_nodes(doc, './/ThreadGroup')
    for node in nodes:
        if node.attrib['testname'] != thread_group_name:
            print("can't find thread group")
        else:
            path_loops = './/ThreadGroup[@testname="{}"]/elementProp/stringProp'.format(thread_group_name)
            print(path_loops)
            loops = get_node_by_keyvalue(
                find_nodes(doc, path_loops),
                {"name": "LoopController.loops"})
            change_node_text(loops, "-1")
            path_2 = './/ThreadGroup[@testname="{}"]/stringProp'.format(thread_group_name)
            num_threads1 = get_node_by_keyvalue(
                find_nodes(doc, path_2),
                {"name": "ThreadGroup.num_threads"})
            change_node_text(num_threads1, str(num_threads))
            path_3 = './/ThreadGroup[@testname="{}"]/stringProp'.format(thread_group_name)
            ramp_time1 = get_node_by_keyvalue(find_nodes(doc, path_3),
                                              {"name": "ThreadGroup.ramp_time"})
            change_node_text(ramp_time1, str(ramp_time))
            path_4 = './/ThreadGroup[@testname="{}"]/boolProp'.format(thread_group_name)
            scheduler1 = get_node_by_keyvalue(find_nodes(doc, path_4),
                                              {"name": "ThreadGroup.scheduler"})
            change_node_text(scheduler1, "true")
            path_5 = './/ThreadGroup[@testname="{}"]/stringProp'.format(thread_group_name)
            duration1 = get_node_by_keyvalue(find_nodes(doc, path_5),
                                             {"name": "ThreadGroup.duration"})
            change_node_text(duration1, str(duration))
    path = os.path.join(Base_path, "test_results/reports", result_file, run_jmeter_file) + '.jmx'
    write_xml(doc, path)
    os.chdir(result_file)
    print("current path: ", os.getcwd())

    # Check environment variables
    if isEvn():
        # Determine distributed execution mode
        if len(host_ips.split(",")) > 2:
            # Add execution types according to your needs
            Rcmd = 'jmeter -n -t %s.jmx -R %s -l %s.jtl -j %s.log' % (
                run_jmeter_file, host_ips, run_jmeter_file, run_jmeter_file)

            print('execute command 1：%s' % Rcmd)
            # os.system(Rcmd)
        else:
            # Automatically generate html reports
            cmd = 'jmeter  -n -t %s.jmx -l %s.jtl -j %s.log -e -o %s' % (
                run_jmeter_file, run_jmeter_file, run_jmeter_file, run_jmeter_file)
            print('execute command 2：%s' % cmd)
            os.system(cmd)


def isEvn():
    '''
    Check environment variables
    :return: True/False
    '''

    cmd = 'jmeter -v'
    lin = os.popen(cmd)
    for i in lin:
        if 'The Apache Software Foundation' in i:
            print("Jmeter environment variables configured successfully")
            return True
    else:
        print("Jmeter environment variable configuration failed")
        return False


if __name__ == '__main__':
    # Distributed ip writing, multiple separated by commas
    host_ips = '127.0.0.1'
    thread_group_name = 'Thread Group'
    if len(sys.argv[1:]) == 5:
        print('The number of parameters is:', len(sys.argv), 'parameters.')
        print('List of available parameters:', str(sys.argv[1:]))
        param = sys.argv[1:]
        print("script name: %s,Concurrency: %s,step size: %s,execution time: %s,Remark: %s" % (
            param[0], param[1], param[2], param[3], param[4]))
        jmeter_number(param[0], param[1], param[2], param[3], param[4], thread_group_name, host_ips)
    elif len(sys.argv[1:]) == 6:
        print('The number of parameters is:', len(sys.argv), 'parameters.')
        print('List of available parameters:', str(sys.argv[1:]))
        param = sys.argv[1:]
        print("script name: %s,Concurrency: %s,step size: %s,execution time: %s,Remark: %s,thread_group_name: %s" % (
            param[0], param[1], param[2], param[3], param[4], param[5]))
        jmeter_number(param[0], param[1], param[2], param[3], param[4], param[5], host_ips)
    else:
        print("parameter is wrong")
    pass
    # jmeter_number('HTTP_Request', 2, 1, 30, 'pythontest778', 'Thread_Group1')
    # command :python startJmeter.py HTTP_Request 2 1 30 pythontest
