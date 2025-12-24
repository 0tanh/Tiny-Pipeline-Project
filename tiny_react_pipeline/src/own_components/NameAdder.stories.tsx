import React from 'react';
import type {Meta, StoryObj} from '@storybook/react';

import NameAdder from './NameAdder';

const meta: Meta<typeof NameAdder> = {
  component: NameAdder,
};

export default meta;

type Story = StoryObj<typeof NameAdder>;

export const Basic: Story = {args: {}};
