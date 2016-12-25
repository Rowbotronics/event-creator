# -*- coding: utf-8 -*-

import logging

import ui

from plugins import Plugin

class MakerspaceAuthorizationsPlugin(Plugin):
	def __init__(self):
		super().__init__('MakerspaceAuthorizations')

		self.options = [
			{
				'name': 'Authorization list',
				'type': 'text',
			}
		]
		if self.getSetting('Authorization list') != '':
			auths = self.getSetting('Authorization list').split(',')
			auths.sort()
			ui.addTagGroup('Required auth\'s', auths)
			
		ui.addTarget(self.name, self, self.updateDescription)
		
	def updateDescription(self, event):
		logging.debug('Adding authorizations to description')
		
		auths = event['tags']['Required auth\'s']
		if len(auths) > 0:
			event['description'] += '\n\nRequired authorizations: ' + ','.join(auths)

def load():
	return MakerspaceAuthorizationsPlugin()